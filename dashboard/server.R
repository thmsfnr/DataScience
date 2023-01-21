
library(shiny)
library(ggplot2)

price <- read.csv("./www/conclusion.csv", header = TRUE)
pollution <- read.csv("./www/CO2_emissions_for_R.csv", header = TRUE)
production <- read.csv("./www/df_production.csv",header = TRUE)
consommation <- read.csv("./www/df_consommation.csv", header = TRUE)

# Server logic
shinyServer(function(input, output, session) {

  # Use observeEvent to monitor the values of the sliders
  observeEvent(c(input$coal, input$gas, input$hydraulic, input$wind, input$solar, input$oil, input$nuclear), {
    # Get the current sum of the sliders
    sum <- input$coal + input$gas + input$hydraulic + input$wind + input$solar + input$oil + input$nuclear

    # If the sum is greater than 100, adjust the sliders so that the sum is exactly 100
    if (sum > 100) {
      # Get the difference between the current sum and 100
      diff <- sum - 100

      # Subtract proportionnally from each slider
        coal <- input$coal - diff * input$coal / sum
        gas <- input$gas - diff * input$gas / sum
        hydraulic <- input$hydraulic - diff * input$hydraulic / sum
        wind <- input$wind - diff * input$wind / sum
        solar <- input$solar - diff * input$solar / sum
        oil <- input$oil - diff * input$oil / sum
        nuclear <- input$nuclear - diff * input$nuclear / sum

        # Update the sliders
        updateSliderInput(session, "coal", value = coal)
        updateSliderInput(session, "gas", value = gas)
        updateSliderInput(session, "hydraulic", value = hydraulic)
        updateSliderInput(session, "wind", value = wind)
        updateSliderInput(session, "solar", value = solar)
        updateSliderInput(session, "oil", value = oil)
        updateSliderInput(session, "nuclear", value = nuclear)
    }
  })

  # Use observeEvent to clear the sliders
  observeEvent(input$clear, {
    # Update the sliders
        updateSliderInput(session, "coal", value = 0)
        updateSliderInput(session, "gas", value = 0)
        updateSliderInput(session, "hydraulic", value = 0)
        updateSliderInput(session, "wind", value = 0)
        updateSliderInput(session, "solar", value = 0)
        updateSliderInput(session, "oil", value = 0)
        updateSliderInput(session, "nuclear", value = 0)
  })

  # Use observeEvent to reset the sliders
  observeEvent(input$reset, {
    # Update the sliders
        updateSliderInput(session, "coal", value = 2)
        updateSliderInput(session, "gas", value = 7)
        updateSliderInput(session, "hydraulic", value = 9)
        updateSliderInput(session, "wind", value = 2)
        updateSliderInput(session, "solar", value = 2)
        updateSliderInput(session, "oil", value = 2)
        updateSliderInput(session, "nuclear", value = 76)
  })

  output$prix <- renderText({

    df <- price

    # Simulate whithout nuclear (part of ther increase proportionally the ols shares)
    newPartProduction <- c(Charbon = input$coal, Gaz = input$gas, Hydraulique = input$hydraulic, Eolien = input$wind, Solaire = input$solar, Fioul = input$oil, Nucléaire = input$nuclear)

    # Calculate a factor for each filiere using newPartProduction variable
    for (i in 1:nrow(df)) {
      ratio <- (df$part_de_production[i] / (newPartProduction[df$filiere[i]]))
      ratio <- ratio - (ratio - 1) * 0.9
      df$factor[i] <- ratio
    }

    # Add the new production part
    for (i in 1:nrow(df)) {
      df$part_de_production[i] <- newPartProduction[df$filiere[i]]
    }

    # Replace the old price by the new price
    for (i in 1:nrow(df)) {
      price <- df$prix_MWh[i] * df$factor[i]
      df$prix_MWh[i] <- price
    }

    # Calculate the electricity price
    priceNuclear <- 0
    for (i in 1:nrow(df)) {
      # if part de production is different from 0
      if (df$part_de_production[i] != 0) {
        priceNuclear <- priceNuclear + df$prix_MWh[i] * (df$part_de_production[i]/100)
      }
    }

    paste("Coût de production moyen:",round(priceNuclear,2),"€/MWh")
  })

  output$environnement <- renderText({

    df <- price

    # Simulate whithout nuclear (part of ther increase proportionally the ols shares)
    newPartProduction <- c(Charbon = input$coal, Gaz = input$gas, Hydraulique = input$hydraulic, Eolien = input$wind, Solaire = input$solar, Fioul = input$oil, Nucléaire = input$nuclear)

    # Add the new production part
    for (i in 1:nrow(df)) {
      df$part_de_production[i] <- newPartProduction[df$filiere[i]]
    }

    # Calculate the electricity pollution
    pollutionNuclear <- 0
    for (i in 1:nrow(df)) {
      pollutionNuclear <- pollutionNuclear + (df$part_de_production[i]/100) * pollution$CO2_emissions[i]
    }

    paste("Émissions de CO2 moyennes:",round(pollutionNuclear,3),"kgCO2/MWh")
  })

  output$mix <- renderImage({
    list(src = "./www/mix_2050.png")
  })

  output$production <- renderPlot({
    
    df_production <- reactive({subset(production,annee >= input$anneeLim[1] & annee <= input$anneeLim[2] & filiere %in% input$filieres)})
    if(input$typeDiagramme == "histogramme"){
      ggplot(df_production(), aes(x=annee,y=production_electricite_MWh, fill = filiere))+
        geom_col()+
        ggtitle(label= "Évolution de la production d'électricité (en MWh) en fonction des années par filière")+
        labs(x="Année",y = "Production d'électricité (en MWh)", color="Filières")
    }
    else if (input$typeDiagramme == "courbe") {
      ggplot(df_production()) + geom_line(
        aes(x = annee, y = production_electricite_MWh,
            color = filiere,
        )
      )+
        xlab("Années")+
        ylab("Production en électricité (en MWh)")+
        ggtitle("Évolution de la production d'électricité (en MWh) en fonction des années par filière")
    }
  })

  output$grapheConsommation <- renderPlot({
    if (input$secteurConsommation != "totale") {
      titlelab = paste("Consommation d'électricité (en MWh) en France, dans le secteur ", input$secteurConsommation, ", en fonction des années", sep="")
    } else {
      titlelab = "Consommation d'électricité (en MWh) en France, en fonction des années"
    }

    graph_conso = ggplot(consommation, aes_string(x="annee", y=paste("conso_", input$secteurConsommation, sep=""))) +
      labs(title = titlelab,
          x = "Année",
          y = "Consommation d'électricité (en MWh)")

    if ("ligne" %in% input$graph_consommation_choices) graph_conso = graph_conso + geom_line()
    if ("tendance" %in% input$graph_consommation_choices) graph_conso = graph_conso + geom_smooth(method = "lm",formula = 'y ~ x')
    if ("points" %in% input$graph_consommation_choices) graph_conso = graph_conso + geom_point()

    graph_conso
  })
  
  output$prediction_production <- renderImage({
      if(input$choix_prediction_filiere == "bioénergie"){
        list(src = "./www/prevision-bioenergie.png") 
      }
      else if (input$choix_prediction_filiere == "charbon"){
        list(src = "./www/prediction-charbon.png") 
      }
      else if(input$choix_prediction_filiere == "éolien"){
        list(src = "./www/prevision-production-eolien.png") 
      }
      else if(input$choix_prediction_filiere == "gaz"){
        list(src = "./www/prevision-production-gaz.png") 
      }
      else if(input$choix_prediction_filiere == "hydraulique"){
        list(src = "./www/prevision-production-hydraulique.png") 
      }
      else if(input$choix_prediction_filiere == "nucléaire"){
        list(src = "./www/prevision-nucleaire.png") 
      }
      else if (input$choix_prediction_filiere == "solaire"){
        list(src = "./www/prevision-solaire.png") 
      }
  })

  output$predictionConsommation <- renderImage({
    if (input$secteurConsommation == "totale") {
      list(src = "./www/global-consommation-prevision.png")
    } else {
      list(src = paste("./www/", input$secteurConsommation, "-consommation-prevision.png", sep=""))
    }
  })
  
  output$prodConso <- renderPlot({
    df_production <- reactive({subset(production,annee >= 2011 & annee <= 2021 & filiere %in% input$filieres2)})
    
    if (input$secteurConsommation2 != "totale") {
      titlelab = paste("Production et consommation d'électricité (dans le secteur ", input$secteurConsommation2, ") (en MWh) en France, en fonction des années", sep="")
    } else {
      titlelab = "Production et consommation d'électricité (en MWh) en France, en fonction des années"
    }
    
    ggplot() + 
      geom_col(data=df_production(), mapping=aes(x=annee,y=production_electricite_MWh, fill = filiere)) +
      geom_line(data=consommation, mapping=aes_string(x="annee", y=paste("conso_", input$secteurConsommation2, sep=""))) +
      labs(title = titlelab,
           x = "Année",
           y = "Production/Consommation d'électricité (en MWh)")
  })
  
})

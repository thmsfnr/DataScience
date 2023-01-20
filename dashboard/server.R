
library(shiny)
library(ggplot2)
library(palmerpenguins)

price <- read.csv("../analysis-price/conclusion.csv", header = TRUE)
pollution <- read.csv("../analysis-environment/CO2_emissions_for_R.csv", header = TRUE)
production <- read.csv("../cleaneddata/df_production.csv",header = TRUE)
consommation <- read.csv("../cleaneddata/df_consommation.csv", header = TRUE)

# Server logic
shinyServer(function(input, output) {

  output$prixEnvironnement <- renderText({

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
    pollutionNuclear <- 0
    for (i in 1:nrow(df)) {
      priceNuclear <- priceNuclear + df$prix_MWh[i] * (df$part_de_production[i]/100)
      pollutionNuclear <- pollutionNuclear + (df$part_de_production[i]/100) * pollution$CO2_emissions[i]
    }

    paste("Avec ce mix des filières de production d'électricité, nous obtenons un prix moyen de",round(priceNuclear,2),"€/MWh ainsi que des émissions polluantes de",round(pollutionNuclear,3),"kgCO2/MWh.")
  })

  output$rte <- renderImage({
    list(src = "www/RTE_logo.png")
  })

  output$mix <- renderImage({
    list(src = "www/mix_2050.png")
  })

  output$consommation <- renderImage({
    list(src = "www/consommation_2050.png")
  })

  output$production <- renderPlot({
    
    df_production <- reactive({subset(production,annee >= input$anneeLim[1] & annee <= input$anneeLim[2] & filiere %in% input$filieres)})
    ggplot(df_production(), aes(x=annee,y=production_electricite_MWh, fill = filiere))+
      geom_col()+
      ggtitle(label= "Évolution de la production d'électricité (en MWh) en fonction des années par filière")+
      labs(x="Année",y = "Production d'électricité (en MWh)", color="Filières")
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
    if ("tendance" %in% input$graph_consommation_choices) graph_conso = graph_conso + geom_smooth(method = "lm")
    if ("points" %in% input$graph_consommation_choices) graph_conso = graph_conso + geom_point()

    graph_conso
  })
  
  output$predictionConsommation <- renderImage({
    if (input$secteurConsommation == "totale") {
      list(src = "../prevision-consommation/filieres/global-consommation-prevision.png") 
    } else {
      list(src = paste("../prevision-consommation/filieres/", input$secteurConsommation, "-consommation-prevision.png", sep=""))
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

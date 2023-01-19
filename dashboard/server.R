
library(shiny)
library(ggplot2)
library(palmerpenguins)
library(tidyverse)

penguins_nomissing <- na.omit(penguins)
price <- read.csv("../analysis-price/conclusion.csv", header = TRUE)

# Server logic
shinyServer(function(input, output) {

  output$prixEnvironnement <- renderText({

    # Calculate the sum of production part
    sum <- sum(price$part_de_production)

    # Remove nuclear
    df <- price %>% filter(filiere != "Nucléaire")

    # Simulate whithout nuclear (part of ther increase proportionally the ols shares)
    newPartProduction <- c(Charbon = (0.81*sum)/(sum-76.88), Gaz = (7.0*sum)/(sum-76.88), Hydraulique = (8.56*sum)/(sum-76.88), Eolien = (0.7647861595767812*sum)/(sum-76.88), Solaire = (0.0787807345745655*sum)/(sum-76.88), Fioul = (0.8*sum)/(sum-76.88))

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
      priceNuclear <- priceNuclear + df$prix_MWh[i] * (df$part_de_production[i]/100)
    }


    paste("Prix:",priceNuclear,"€")
  })

  # Plot of flipper length
  output$fliperPlot <- renderPlot({

    # If Espèce is selected
    if (input$varChoice == "Espèce") {
      ggplot(subset(penguins_nomissing, species %in% input$species & flipper_length_mm >= input$xlim[1] & flipper_length_mm <= input$xlim[2]),aes(x = flipper_length_mm,fill = species)) +
      geom_histogram(stat="count") +
      labs(x = "Taille des ailes (mm)",y="Nombre de manchots",title = "Répartition des manchots selon la taille de leurs ailes.")
    }

    # If Sexe is selected
    else if (input$varChoice == "Sexe") {
      ggplot(subset(penguins_nomissing, flipper_length_mm >= input$xlim[1] & flipper_length_mm <= input$xlim[2]),aes(x = flipper_length_mm,fill = sex)) +
      geom_histogram(stat="count") +
      labs(x = "Taille des ailes (mm)",y="Nombre de manchots",title = "Répartition des manchots selon la taille de leurs ailes.")
    }
  })

  # Plot of bill length
  output$billPlot <- renderPlot({

    # If Espèce is selected
    if (input$varChoice == "Espèce") {
      ggplot(subset(penguins_nomissing, species %in% input$species & bill_length_mm >= input$ylim[1] & bill_length_mm <= input$ylim[2]),aes(x = bill_length_mm,fill = species)) +
      geom_histogram(stat="count")+
      labs(x = "Longeur du bec (mm)",y="Nombre de manchots",title = "Répartition des manchots selon la longeur de leur bec.")
    }

    # If Sexe is selected
    else if (input$varChoice == "Sexe") {
      ggplot(subset(penguins_nomissing, bill_length_mm >= input$ylim[1] & bill_length_mm <= input$ylim[2]),aes(x = bill_length_mm,fill = sex)) +
      geom_histogram(stat="count")+
      labs(x = "Longeur du bec (mm)",y="Nombre de manchots",title = "Répartition des manchots selon la longeur de leur bec.")
    }

  })

  # Plot of bill depth
  output$bill2Plot <- renderPlot({

    # If Espèce is selected
    if (input$varChoice == "Espèce") {
      ggplot(subset(penguins_nomissing, species %in% input$species & bill_depth_mm >= input$zlim[1] & bill_depth_mm <= input$zlim[2]),aes(x = bill_depth_mm,fill = species)) +
      geom_histogram(stat="count")+
      labs(x = "Profondeur du bec (mm)",y="Nombre de manchots",title = "Répartition des manchots selon la profondeur de leur bec.")
    }

    # If Sexe is selected
    else if (input$varChoice == "Sexe") {
      ggplot(subset(penguins_nomissing, bill_depth_mm >= input$zlim[1] & bill_depth_mm <= input$zlim[2]),aes(x = bill_depth_mm,fill = sex)) +
      geom_histogram(stat="count")+
      labs(x = "Profondeur du bec (mm)",y="Nombre de manchots",title = "Répartition des manchots selon la profondeur de leur bec.")
    }

  })

  # Plot of mass
  output$massPlot <- renderPlot({

    # If Espèce is selected
    if (input$varChoice == "Espèce") {
      ggplot(subset(penguins_nomissing, species %in% input$species & body_mass_g >= input$wlim[1] & body_mass_g <= input$wlim[2]),aes(x = body_mass_g,fill = species)) +
      geom_histogram(stat="count")+
      labs(x = "Masse (g)",y="Nombre de manchots",title = "Répartition des manchots selon leur masse.")
    }

    # If Sexe is selected
    else if (input$varChoice == "Sexe") {
      ggplot(subset(penguins_nomissing, body_mass_g >= input$wlim[1] & body_mass_g <= input$wlim[2]),aes(x = body_mass_g,fill = sex)) +
      geom_histogram(stat="count")+
      labs(x = "Masse (g)",y="Nombre de manchots",title = "Répartition des manchots selon leur masse.")
    }

  })

  # Plot of islands
  output$islandPlot <- renderPlot({

    # If Espèce is selected
    if (input$varChoice == "Espèce") {
      ggplot(subset(penguins_nomissing, species %in% input$species),aes(x = island,fill = species)) +
      geom_histogram(stat="count")+
      labs(x = "Nom de l'ile",y="Nombre de manchots",title = "Répartition des manchots pour chaque ile.")
    }

    # If Sexe is selected
    else if (input$varChoice == "Sexe") {
      ggplot(subset(penguins_nomissing, species %in% input$species),aes(x = island,fill = sex)) +
      geom_histogram(stat="count")+
      labs(x = "Nom de l'ile",y="Nombre de manchots",title = "Répartition des manchots pour chaque ile.")
    }
  })

})

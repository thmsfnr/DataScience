
library(shiny)
library(ggplot2)
library(palmerpenguins)
library(tidyverse)

penguins_nomissing <- na.omit(penguins)
price <- read.csv("../analysis-price/conclusion.csv", header = TRUE)
pollution <- read.csv("../analysis-environment/CO2_emissions_for_R.csv", header = TRUE)

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

  output$rte <- renderImage({
    list(src = "www/RTE_logo.png")
  })
  
  output$mix <- renderImage({
    list(src = "www/mix_2050.png")
  })

  output$consommation <- renderImage({
    list(src = "www/consommation_2050.png")
  })

  output$introduction <- renderText({
    paste("L'objectif de ce projet est de réaliser une application Shiny permettant de visualiser les données de la base de données penguins de R. Cette base de données contient des informations sur les manchots de l'Antarctique. Les données sont disponibles sur le site de R :")
  })

  output$mix2030 <- renderText({
    paste("La consommation d'électricité en France en 2030 est estimée à 400 TWh. La production d'électricité en France en 2030 est estimée à 400 TWh. La consommation d'électricité en France en 2050 est estimée à 500 TWh. La production d'électricité en France en 2050 est estimée à 500 TWh.")
  })

  output$consommation2030 <- renderText({
    paste("La consommation d'électricité en France en 2030 est estimée à 400 TWh. La production d'électricité en France en 2030 est estimée à 400 TWh. La consommation d'électricité en France en 2050 est estimée à 500 TWh. La production d'électricité en France en 2050 est estimée à 500 TWh.")
  })


})

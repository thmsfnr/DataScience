
library(shiny)
library(ggplot2)
library(palmerpenguins)
includeCSS("./style.css")

penguins_nomissing <- na.omit(penguins)

# Server logic
shinyServer(function(input, output) {

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


library(shiny)
library(ggplot2)

price <- read.csv("../analysis-price/conclusion.csv", header = TRUE)
pollution <- read.csv("../analysis-environment/CO2_emissions_for_R.csv", header = TRUE)

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
      priceNuclear <- priceNuclear + df$prix_MWh[i] * (df$part_de_production[i]/100)
    }

    paste("Cout de production moyen:",round(priceNuclear,2),"€/MWh")
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

    paste("Emmissions de CO2 moyennes:",round(pollutionNuclear,3),"kgCO2/MWh")
  })

  output$mix <- renderImage({
    list(src = "./mix_2050.png")
  })

})

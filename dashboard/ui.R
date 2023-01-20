
library(shiny)
library(shinythemes)

# Define UI for the application
shinyUI(fluidPage(
  title = "Énergie en France",
  theme = shinytheme("superhero"),
  
  tags$head(tags$style(
    type="text/css",
    "#predictionConsommation img {max-width: 100%; height: auto}
    #grapheConsommation {max-width: 800px; width: 100%;}
    "
  )),

  # Application header
  titlePanel(h2(align="center","Énergie en France")),
  fluidRow(h4(align="center","Ce projet est une analyse de la sortie du nucléaire dans la production d'électricité française réalisée lors d'un cours à Polytech Montpellier.")),
  fluidRow(h3("")),

  sidebarLayout(

    # Sidebar
    sidebarPanel(

      # More information about the project
      p("Ce projet visait initialement à nous permettre d'approfondir certaines connaissances acquises au cours de notre formation, d'en découvrir d'autres, d'identifier des méthodes appropriées pour répondre à un objectif donné, de combiner des méthodes complémentaires, de comparer des méthodes concurrentes pour répondre à des objectifs donnés, d'interpréter et éventuellement de comparer les résultats des méthodes mises en œuvre, ainsi que d'avoir un esprit critique vis-à-vis de la collecte des données, des méthodes mises en œuvre et de leur paramétrage."),
      p("Concernant le sujet, nous avions le choix entre différents thèmes et nous avons choisi celui lié à l'étude des données ouvertes, plus précisément lié au projet d'Université des données ouvertes mené par l'association Latitudes en lien avec le site institutionnel national data gouv. Les jeux de données de ce thème sont alors multiples, sachant que nous avons fait le choix d'étudier celui associé à l'énergie en France."),
      p("Concernant la problématique, nous en avons choisi une qui diffère de celle proposée dans le projet. Au lieu de centrer notre étude sur les conséquences énergétiques de la guerre en Ukraine, nous allons déterminer les conséquences de la fin du nucléaire dans la production d'électricité en France."),
      a(href = "https://github.com/thmsfnr/DataScience", "Cliquez ici pour plus d'informations"),
      tags$hr(style = "border:0.8px solid white;"),

      # If "Conséquences sur le prix et l'environnement" is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Conséquences sur prix et environnement'",
        h5(align="center","Choix de la répartition des différentes filières de production"),
        sliderInput("hydraulic","Hydraulique:",min = 0, max = 100,value = c(10)),
        sliderInput("nuclear","Nucléaire:",min = 0, max = 100,value = c(10)),
        sliderInput("wind","Eolien:",min = 0, max = 100,value = c(10)),
        sliderInput("solar","Photovolatique:",min = 0, max = 100,value = c(10)),
        sliderInput("gas","Gaz:",min = 0, max = 100,value = c(10)),
        sliderInput("coal","Charbon:",min = 0, max = 100,value = c(10)),
        sliderInput("oil","Fioul:",min = 0, max = 100,value = c(10)),
      ),

      # If "Production" is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Production'",

      ),

      # If "Consommation" is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Consommation'",
        checkboxGroupInput(inputId = "graph_consommation_choices",
                           label = "Modifier le graphique",
                           choices = c("Courbe de tendance" = "tendance",
                                        "Afficher les points" = "points",
                                        "Afficher la ligne" = "ligne"),
                           selected= c("tendance", "points", "ligne")
        ),
        radioButtons("secteurConsommation", "Choix du secteur",
                     choices = c("totale", "agriculture",
                                 "industrie", "tertiaire",
                                 "residentiel", "secteur_inconnu"),
                     selected="totale"),
      ),

      # If "Lien entre production et consommation" is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Lien entre production et consommation'",

      ),

      # If "Confrontation des prédictions" is selected
      conditionalPanel(
        condition = "input.tabSelected == 'Confrontation des prédictions'",

      )
    ),

    # Main
    mainPanel(
      navbarPage("Menu",id = "tabSelected",

        # Display of graphics according to the selected menu
        navbarMenu("Fenetres",
          tabPanel("Conséquences sur prix et environnement", h3(textOutput("prixEnvironnement")),),
          tabPanel("Production",),
          tabPanel("Consommation", div(plotOutput("grapheConsommation"), 
                                       h4("Prédiction des valeurs jusqu'en 2030 avec Prophet"),
                                       #imageOutput("predictionConsommation", width="100%", height="auto"))),
                                       imageOutput("predictionConsommation"))),
          tabPanel("Lien entre production et consommation",),
          tabPanel("Confrontation des prédictions",
          column(6,
            imageOutput("rte"), p("hjdfjdhf"), imageOutput("mix"), p("hjdfjdhf"), imageOutput("consommation"), p("hjsgfhjs")
          )),
        )
      )
    )

  )
))

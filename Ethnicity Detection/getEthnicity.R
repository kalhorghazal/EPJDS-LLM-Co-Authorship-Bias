"""# Import Libraries """

install.packages("openxlsx")

library(readxl)
library(openxlsx)

if (!requireNamespace("devtools", quietly = TRUE)) {
  install.packages("devtools")
}

devtools::install_github("fangzhou-xie/rethnicity")

library(rethnicity)

data <- read.csv("uniqueNames.csv")

"""# Detect Ethnicities"""

predict_multiple_ethnicities <- function(names_lists) {
  results <- list()

  for (names in names_lists) {

    names <- na.omit(names)

    if (length(names) == 0) {
      results[[length(results) + 1]] <- character(0)
      next
    }


    split_names <- function(full_name) {
      name_parts <- unlist(strsplit(full_name, " "))
      if (length(name_parts) >= 2) {
        first_name <- name_parts[1]
        last_name <- paste(name_parts[-1], collapse = " ")
      } else {
        first_name <- full_name
        last_name <- ""
      }
      return(c(first_name, last_name))
    }


    names_split <- t(sapply(names, split_names))
    firstnames <- names_split[, 1]
    lastnames <- names_split[, 2]


    no_last_name_indices <- which(lastnames == "")
    if (length(no_last_name_indices) > 0) {
      lastnames[no_last_name_indices] <- "Unknown"
    }

    # Predict ethnicity using the rethnicity package
    predictions <- predict_ethnicity(firstnames, lastnames, method = "fullname")

    # Extract predicted ethnicities and combine into a single vector
    ethnicities_combined <- sapply(predictions$race, function(eth) paste(eth, collapse = ", "))

    results[[length(results) + 1]] <- ethnicities_combined
  }

  return(results)
}

"""## Get Authors' Ethnicity"""

authorsNames <- data[["Name"]]
authorsNames <- lapply(authorsNames, function(names) trimws(names))

authorsEthnicities <- predict_multiple_ethnicities(authorsNames)
data$'Ethnicity' <- sapply(authorsEthnicities, function(eth) paste(eth, collapse = "/"))

summary(data)

write.xlsx(data, "uniqueNames.xlsx", sheetName = "Sheet1", colNames = TRUE, rowNames = FALSE, append = TRUE)
-- Select genre name and the number of linked shows
SELECT 
    genres.name AS genre,  -- First column: Genre name, labeled as "genre"
    COUNT(tv_show_genres.show_id) AS number_of_shows  -- Second column: Count of linked shows, labeled as "number_of_shows"
    
-- Main table from which genres are selected
FROM 
    genres

-- Inner join to match each genre to its linked shows in the tv_show_genres table
INNER JOIN 
    tv_show_genres ON genres.id = tv_show_genres.genre_id

-- Group results by genre name to count linked shows for each genre
GROUP BY 
    genres.id, genres.name  -- Group by genre id and name to avoid issues with ONLY_FULL_GROUP_BY mode

-- Sort the results in descending order of the number of linked shows
ORDER BY 
    number_of_shows DESC;

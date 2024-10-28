-- Select the genre name and count of linked shows
SELECT 
    genres.name AS genre,  -- First column: Genre name, aliased as "genre"
    COUNT(tv_show_genres.show_id) AS number_of_shows  -- Second column: Count of linked shows, aliased as "number_of_shows"
    
-- Specify the tables involved in the query
FROM 
    genres

-- Join the tv_show_genres table to link genres with their respective shows
INNER JOIN 
    tv_show_genres ON genres.id = tv_show_genres.genre_id

-- Group results by genre to get the count for each genre
GROUP BY 
    genres.name

-- Sort results in descending order based on the count of linked shows
ORDER BY 
    number_of_shows DESC;

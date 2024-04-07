from fastapi import FastAPI, HTTPException
import json
import requests

app = FastAPI()


graphql_url = 'https://leetcode.com/graphql'

@app.get("/user_public_profile/{username}")
def get_user_public_profile(username: str):
    '''
    Get the public profile of a user
    @param username: the username of the user
    @return: the public profile of the user
    '''
    query = """
    query userPublicProfile($username: String!) {
        matchedUser(username: $username) {
            username
            submitStats: submitStatsGlobal {
                acSubmissionNum {
                    difficulty
                    count
                    submissions
                }
            }
        }
    }
    """
    variables = {"username": username}
    response = requests.post(graphql_url, json={'query': query, 'variables': variables}, headers={'Content-Type': 'application/json'})
    return response.json()

@app.get("/user_detailed_public_profile/{username}")
def get_user_detailed_public_profile(username: str):
    '''
    Get the detailed public profile of a user
    @param username: the username of the user
    @return: the detailed public profile of the user
    '''

    query = """
    query userPublicProfile($username: String!) {
        matchedUser(username: $username) {
            contestBadge {
                name
                expired
                hoverText
                icon
            }
            username
            githubUrl
            twitterUrl
            linkedinUrl
            profile {
                ranking
                userAvatar
                realName
                aboutMe
                school
                websites
                countryName
                company
                jobTitle
                skillTags
                postViewCount
                postViewCountDiff
                reputation
                reputationDiff
                solutionCount
                solutionCountDiff
                categoryDiscussCount
                categoryDiscussCountDiff
            }
        }
    }
    """
    variables = {"username": username}
    response = requests.post(graphql_url, json={'query': query, 'variables': variables}, headers={'Content-Type': 'application/json'})
    return response.json()

@app.get("/user_language_stats/{username}")
def get_user_language_stats(username: str):
    '''
    Get the language stats of a user
    @param username: the username of the user
    @return: the language stats of the user
    '''

    query = """
    query languageStats($username: String!) {
        matchedUser(username: $username) {
            languageProblemCount {
                languageName
                problemsSolved
            }
        }
    }
    """
    variables = {"username": username}
    response = requests.post(graphql_url, json={'query': query, 'variables': variables}, headers={'Content-Type': 'application/json'})
    return response.json()


@app.get("/user_skill_stats/{username}")
def get_user_skill_stats(username: str):
    '''
    Get the skill stats of a user
    @param username: the username of the user
    @return: the skill stats of the user
    '''
    
    query = """
    query skillStats($username: String!) {
        matchedUser(username: $username) {
            tagProblemCounts {
                advanced {
                    tagName
                    tagSlug
                    problemsSolved
                }
                intermediate {
                    tagName
                    tagSlug
                    problemsSolved
                }
                fundamental {
                    tagName
                    tagSlug
                    problemsSolved
                }
            }
        }
    }
    """
    variables = {"username": username}
    response = requests.post(graphql_url, json={'query': query, 'variables': variables}, headers={'Content-Type': 'application/json'})
    return response.json()

@app.get("/user_contest_ranking_info/{username}")
def get_user_contest_ranking_info(username: str):
    '''
    Get the contest ranking info of a user
    @param username: the username of the user
    @return: the contest ranking info of the user
    '''
    
    query = """
    query userContestRankingInfo($username: String!) {
        userContestRanking(username: $username) {
            attendedContestsCount
            rating
            globalRanking
            totalParticipants
            topPercentage
            badge {
                name
            }
        }
        userContestRankingHistory(username: $username) {
            attended
            trendDirection
            problemsSolved
            totalProblems
            finishTimeInSeconds
            rating
            ranking
            contest {
                title
                startTime
            }
        }
    }
    """
    variables = {"username": username}
    response = requests.post(graphql_url, json={'query': query, 'variables': variables}, headers={'Content-Type': 'application/json'})
    return response.json()

@app.get("/user_problems_solved/{username}")
def get_user_problems_solved(username: str):
    '''
    Get the problems solved by a user
    @param username: the username of the user
    @return: the problems solved by the user
    '''
    
    query = """
    query userProblemsSolved($username: String!) {
        allQuestionsCount {
            difficulty
            count
        }
        matchedUser(username: $username) {
            problemsSolvedBeatsStats {
                difficulty
                percentage
            }
            submitStatsGlobal {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
    }
    """
    variables = {"username": username}
    response = requests.post(graphql_url, json={'query': query, 'variables': variables}, headers={'Content-Type': 'application/json'})
    return response.json()

@app.get("/user_profile_calendar/{username}/{year}")
def get_user_profile_calendar(username: str, year: int):
    '''
    Get the profile calendar of a user
    @param username: the username of the user
    @param year: the year of the calendar
    @return: the profile calendar of the user
    '''
    
    query = """
    query userProfileCalendar($username: String!, $year: Int) {
        matchedUser(username: $username) {
            userCalendar(year: $year) {
                activeYears
                streak
                totalActiveDays
                dccBadges {
                    timestamp
                    badge {
                        name
                        icon
                    }
                }
                submissionCalendar
            }
        }
    }
    """
    variables = {"username": username, "year": year}
    response = requests.post(graphql_url, json={'query': query, 'variables': variables}, headers={'Content-Type': 'application/json'})
    return response.json()




# Add more endpoints for other queries here

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=4999)

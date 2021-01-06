{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>quantity</th>\n",
       "      <th>item_name</th>\n",
       "      <th>choice_description</th>\n",
       "      <th>item_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Chips and Fresh Tomato Salsa</td>\n",
       "      <td>NaN</td>\n",
       "      <td>$2.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Izze</td>\n",
       "      <td>[Clementine]</td>\n",
       "      <td>$3.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Nantucket Nectar</td>\n",
       "      <td>[Apple]</td>\n",
       "      <td>$3.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Chips and Tomatillo-Green Chili Salsa</td>\n",
       "      <td>NaN</td>\n",
       "      <td>$2.39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>Chicken Bowl</td>\n",
       "      <td>[Tomatillo-Red Chili Salsa (Hot), [Black Beans...</td>\n",
       "      <td>$16.98</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   order_id  quantity                              item_name  \\\n",
       "0         1         1           Chips and Fresh Tomato Salsa   \n",
       "1         1         1                                   Izze   \n",
       "2         1         1                       Nantucket Nectar   \n",
       "3         1         1  Chips and Tomatillo-Green Chili Salsa   \n",
       "4         2         2                           Chicken Bowl   \n",
       "\n",
       "                                  choice_description item_price  \n",
       "0                                                NaN     $2.39   \n",
       "1                                       [Clementine]     $3.39   \n",
       "2                                            [Apple]     $3.39   \n",
       "3                                                NaN     $2.39   \n",
       "4  [Tomatillo-Red Chili Salsa (Hot), [Black Beans...    $16.98   "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df=pd.read_table('http://bit.ly/chiporders')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userid</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>occupation</th>\n",
       "      <th>zip_code</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>24</td>\n",
       "      <td>M</td>\n",
       "      <td>technician</td>\n",
       "      <td>85711</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>53</td>\n",
       "      <td>F</td>\n",
       "      <td>other</td>\n",
       "      <td>94043</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>23</td>\n",
       "      <td>M</td>\n",
       "      <td>writer</td>\n",
       "      <td>32067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>24</td>\n",
       "      <td>M</td>\n",
       "      <td>technician</td>\n",
       "      <td>43537</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>33</td>\n",
       "      <td>F</td>\n",
       "      <td>other</td>\n",
       "      <td>15213</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   userid  age gender  occupation zip_code\n",
       "0       1   24      M  technician    85711\n",
       "1       2   53      F       other    94043\n",
       "2       3   23      M      writer    32067\n",
       "3       4   24      M  technician    43537\n",
       "4       5   33      F       other    15213"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user_list=['userid','age','gender','occupation','zip_code']\n",
    "df2=pd.read_table('http://bit.ly/movieusers',sep='|',header=None,names=user_list)\n",
    "df2.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['userid', 'age', 'gender', 'occupation', 'zip_code'], dtype='object')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method NDFrame.describe of      userid  age gender     occupation zip_code\n",
       "0         1   24      M     technician    85711\n",
       "1         2   53      F          other    94043\n",
       "2         3   23      M         writer    32067\n",
       "3         4   24      M     technician    43537\n",
       "4         5   33      F          other    15213\n",
       "..      ...  ...    ...            ...      ...\n",
       "938     939   26      F        student    33319\n",
       "939     940   32      M  administrator    02215\n",
       "940     941   20      M        student    97229\n",
       "941     942   48      F      librarian    78209\n",
       "942     943   22      M        student    77841\n",
       "\n",
       "[943 rows x 5 columns]>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.describe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(14, 5)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df3=df2[(df2['age']<=30) & (df2['occupation']=='technician') & (df2['gender']=='M')]\n",
    "df3.head()\n",
    "df3.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(273, 5)"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[df2['gender']=='F'].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(670, 5)"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[df2['gender']=='M'].shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(943, 5)"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['technician', 'other', 'writer', 'executive', 'administrator',\n",
       "       'student', 'lawyer', 'educator', 'scientist', 'entertainment',\n",
       "       'programmer', 'librarian', 'homemaker', 'artist', 'engineer',\n",
       "       'marketing', 'none', 'healthcare', 'retired', 'salesman', 'doctor'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2['occupation'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 5)"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[(df2['occupation']=='technician') & (df2['gender']=='F') ].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(28, 5)"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[(df2['occupation']=='scientist') & (df2['gender']=='M') ].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(22, 5)"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[(df2['occupation']=='librarian') & (df2['gender']=='M') ].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(29, 5)"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[(df2['occupation']=='librarian') & (df2['gender']=='M') ].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(11, 5)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[(df2['occupation']=='healthcare') & (df2['gender']=='F') ].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5, 5)"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[(df2['occupation']=='healthcare') & (df2['gender']=='M') ].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(69, 5)"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[(df2['occupation']=='educator') & (df2['gender']=='M') ].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(26, 5)"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2[(df2['occupation']=='educator') & (df2['gender']=='F') ].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_count(param):\n",
    "    return df2[(df2['occupation']==param) & (df2['gender']=='M')].shape[0]\n",
    "\n",
    "l=df2['occupation'].unique()\n",
    "l=list(l)\n",
    "k=map(lambda x:(x,df2[(df2['occupation']==x) & (df2['gender']=='M')].shape[0]),l)\n",
    "m=map(lambda x:(x,df2[(df2['occupation']==x) & (df2['gender']=='F')].shape[0]),l)\n",
    "feamle_movie_goers=dict(list(m))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "male_movie_goers=dict(list(k))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "def comapre_movie_goers(occupation):\n",
    "    return {'male':male_movie_goers[occupation],'female':feamle_movie_goers[occupation]}      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [],
   "source": [
    "movie=[(occupation,comapre_movie_goers(occupation)) for occupation in l]\n",
    "new_movie=dict(movie)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\babiswas'"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import csv\n",
    "file=open('Analysis.csv','w',newline='')\n",
    "writer=csv.DictWriter(file,fieldnames=['occupation','male','female'])\n",
    "writer.writeheader()\n",
    "for key in new_movie.keys():\n",
    "    writer.writerow({'occupation':key,'male':new_movie[key]['male'],'female':new_movie[key]['female']})\n",
    "import os\n",
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>occupation</th>\n",
       "      <th>male</th>\n",
       "      <th>female</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>technician</td>\n",
       "      <td>26</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>other</td>\n",
       "      <td>69</td>\n",
       "      <td>36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>writer</td>\n",
       "      <td>26</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>executive</td>\n",
       "      <td>29</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>administrator</td>\n",
       "      <td>43</td>\n",
       "      <td>36</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>student</td>\n",
       "      <td>136</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>lawyer</td>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>educator</td>\n",
       "      <td>69</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8</td>\n",
       "      <td>scientist</td>\n",
       "      <td>28</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>9</td>\n",
       "      <td>entertainment</td>\n",
       "      <td>16</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>10</td>\n",
       "      <td>programmer</td>\n",
       "      <td>60</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>11</td>\n",
       "      <td>librarian</td>\n",
       "      <td>22</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>12</td>\n",
       "      <td>homemaker</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>13</td>\n",
       "      <td>artist</td>\n",
       "      <td>15</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>14</td>\n",
       "      <td>engineer</td>\n",
       "      <td>65</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>15</td>\n",
       "      <td>marketing</td>\n",
       "      <td>16</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>16</td>\n",
       "      <td>none</td>\n",
       "      <td>5</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>17</td>\n",
       "      <td>healthcare</td>\n",
       "      <td>5</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>18</td>\n",
       "      <td>retired</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>19</td>\n",
       "      <td>salesman</td>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>20</td>\n",
       "      <td>doctor</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       occupation  male  female\n",
       "0      technician    26       1\n",
       "1           other    69      36\n",
       "2          writer    26      19\n",
       "3       executive    29       3\n",
       "4   administrator    43      36\n",
       "5         student   136      60\n",
       "6          lawyer    10       2\n",
       "7        educator    69      26\n",
       "8       scientist    28       3\n",
       "9   entertainment    16       2\n",
       "10     programmer    60       6\n",
       "11      librarian    22      29\n",
       "12      homemaker     1       6\n",
       "13         artist    15      13\n",
       "14       engineer    65       2\n",
       "15      marketing    16      10\n",
       "16           none     5       4\n",
       "17     healthcare     5      11\n",
       "18        retired    13       1\n",
       "19       salesman     9       3\n",
       "20         doctor     7       0"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df5=pd.read_csv('Analysis.csv')\n",
    "df5.head(25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

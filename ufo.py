{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
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
       "      <th>City</th>\n",
       "      <th>Colors Reported</th>\n",
       "      <th>Shape Reported</th>\n",
       "      <th>State</th>\n",
       "      <th>Time</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Ithaca</td>\n",
       "      <td>NaN</td>\n",
       "      <td>TRIANGLE</td>\n",
       "      <td>NY</td>\n",
       "      <td>6/1/1930 22:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Willingboro</td>\n",
       "      <td>NaN</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>NJ</td>\n",
       "      <td>6/30/1930 20:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Holyoke</td>\n",
       "      <td>NaN</td>\n",
       "      <td>OVAL</td>\n",
       "      <td>CO</td>\n",
       "      <td>2/15/1931 14:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Abilene</td>\n",
       "      <td>NaN</td>\n",
       "      <td>DISK</td>\n",
       "      <td>KS</td>\n",
       "      <td>6/1/1931 13:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>New York Worlds Fair</td>\n",
       "      <td>NaN</td>\n",
       "      <td>LIGHT</td>\n",
       "      <td>NY</td>\n",
       "      <td>4/18/1933 19:00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   City Colors Reported Shape Reported State             Time\n",
       "0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00\n",
       "1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00\n",
       "2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00\n",
       "3               Abilene             NaN           DISK    KS   6/1/1931 13:00\n",
       "4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "ufo=pd.read_csv('http://bit.ly/uforeports',sep=',')\n",
    "ufo.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count       18216\n",
       "unique       6476\n",
       "top       Seattle\n",
       "freq          187\n",
       "Name: City, dtype: object"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ufo['City'].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([nan, 'GREEN', 'RED', 'ORANGE', 'BLUE', 'YELLOW', 'RED BLUE',\n",
       "       'GREEN BLUE', 'RED GREEN BLUE', 'ORANGE BLUE'], dtype=object)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ufo[ufo['City']=='Seattle']['Colors Reported'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
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
       "      <th>City</th>\n",
       "      <th>Colors Reported</th>\n",
       "      <th>Shape Reported</th>\n",
       "      <th>State</th>\n",
       "      <th>Time</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>8903</td>\n",
       "      <td>Seattle</td>\n",
       "      <td>RED BLUE</td>\n",
       "      <td>NaN</td>\n",
       "      <td>WA</td>\n",
       "      <td>11/17/1995 23:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8905</td>\n",
       "      <td>Seattle</td>\n",
       "      <td>RED BLUE</td>\n",
       "      <td>NaN</td>\n",
       "      <td>WA</td>\n",
       "      <td>11/17/1995 23:30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>13912</td>\n",
       "      <td>Seattle</td>\n",
       "      <td>RED BLUE</td>\n",
       "      <td>LIGHT</td>\n",
       "      <td>WA</td>\n",
       "      <td>7/10/1999 22:30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          City Colors Reported Shape Reported State              Time\n",
       "8903   Seattle        RED BLUE            NaN    WA  11/17/1995 23:00\n",
       "8905   Seattle        RED BLUE            NaN    WA  11/17/1995 23:30\n",
       "13912  Seattle        RED BLUE          LIGHT    WA   7/10/1999 22:30"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ufo[(ufo['City']=='Seattle') & (ufo['Colors Reported']=='RED BLUE')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
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
       "      <th>City</th>\n",
       "      <th>Colors Reported</th>\n",
       "      <th>Shape Reported</th>\n",
       "      <th>State</th>\n",
       "      <th>Time</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>count</td>\n",
       "      <td>18216</td>\n",
       "      <td>2882</td>\n",
       "      <td>15597</td>\n",
       "      <td>18241</td>\n",
       "      <td>18241</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>unique</td>\n",
       "      <td>6476</td>\n",
       "      <td>27</td>\n",
       "      <td>27</td>\n",
       "      <td>52</td>\n",
       "      <td>16145</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>top</td>\n",
       "      <td>Seattle</td>\n",
       "      <td>RED</td>\n",
       "      <td>LIGHT</td>\n",
       "      <td>CA</td>\n",
       "      <td>11/16/1999 19:00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>freq</td>\n",
       "      <td>187</td>\n",
       "      <td>780</td>\n",
       "      <td>2803</td>\n",
       "      <td>2529</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           City Colors Reported Shape Reported  State              Time\n",
       "count     18216            2882          15597  18241             18241\n",
       "unique     6476              27             27     52             16145\n",
       "top     Seattle             RED          LIGHT     CA  11/16/1999 19:00\n",
       "freq        187             780           2803   2529                27"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ufo.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(18241, 5)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ufo.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Ithaca', 'Willingboro', 'Holyoke', ..., 'Capitola', 'Grant Park',\n",
       "       'Ybor'], dtype=object)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ufo['City'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
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
       "      <th>City</th>\n",
       "      <th>Colors Reported</th>\n",
       "      <th>Shape Reported</th>\n",
       "      <th>State</th>\n",
       "      <th>Time</th>\n",
       "      <th>Location</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Ithaca</td>\n",
       "      <td>NaN</td>\n",
       "      <td>TRIANGLE</td>\n",
       "      <td>NY</td>\n",
       "      <td>6/1/1930 22:00</td>\n",
       "      <td>Ithaca,NY</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Willingboro</td>\n",
       "      <td>NaN</td>\n",
       "      <td>OTHER</td>\n",
       "      <td>NJ</td>\n",
       "      <td>6/30/1930 20:00</td>\n",
       "      <td>Willingboro,NJ</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Holyoke</td>\n",
       "      <td>NaN</td>\n",
       "      <td>OVAL</td>\n",
       "      <td>CO</td>\n",
       "      <td>2/15/1931 14:00</td>\n",
       "      <td>Holyoke,CO</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>Abilene</td>\n",
       "      <td>NaN</td>\n",
       "      <td>DISK</td>\n",
       "      <td>KS</td>\n",
       "      <td>6/1/1931 13:00</td>\n",
       "      <td>Abilene,KS</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>New York Worlds Fair</td>\n",
       "      <td>NaN</td>\n",
       "      <td>LIGHT</td>\n",
       "      <td>NY</td>\n",
       "      <td>4/18/1933 19:00</td>\n",
       "      <td>New York Worlds Fair,NY</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   City Colors Reported Shape Reported State             Time  \\\n",
       "0                Ithaca             NaN       TRIANGLE    NY   6/1/1930 22:00   \n",
       "1           Willingboro             NaN          OTHER    NJ  6/30/1930 20:00   \n",
       "2               Holyoke             NaN           OVAL    CO  2/15/1931 14:00   \n",
       "3               Abilene             NaN           DISK    KS   6/1/1931 13:00   \n",
       "4  New York Worlds Fair             NaN          LIGHT    NY  4/18/1933 19:00   \n",
       "\n",
       "                  Location  \n",
       "0                Ithaca,NY  \n",
       "1           Willingboro,NJ  \n",
       "2               Holyoke,CO  \n",
       "3               Abilene,KS  \n",
       "4  New York Worlds Fair,NY  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ufo['Location']=ufo.City+','+ufo.State\n",
    "ufo.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1889, 6)"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ufo[ufo['Shape Reported']=='TRIANGLE'].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2122, 6)"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ufo[ufo['Shape Reported']=='DISK'].shape"
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
       "'LIGHT'"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l=list(ufo['Shape Reported'].unique())\n",
    "def shape_reported(shape_reported):\n",
    "    return ufo[ufo['Shape Reported']==shape_reported].shape\n",
    "\n",
    "def get_number_differnt_shape(l):\n",
    "    common_shape=dict()\n",
    "    [common_shape.update({i:shape_reported(i)[0]}) for i in l]\n",
    "    return common_shape\n",
    "\n",
    "m=get_number_differnt_shape(l)\n",
    "\n",
    "def get_common_shape_ufo(common_shape):\n",
    "    return max(common_shape,key=common_shape.get)\n",
    "\n",
    "get_common_shape_ufo(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Seattle'"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "city=list(ufo['City'].unique())\n",
    "\n",
    "def city_reported(city):\n",
    "    return ufo[ufo['City']==city].shape[0]\n",
    "\n",
    "def  get_number_city(city):\n",
    "    common_city=dict()\n",
    "    [common_city.update({c:city_reported(c)}) for c in  city]\n",
    "    return common_city\n",
    "\n",
    "def get_city_ufo_common(m):\n",
    "    return max(m,key=m.get)\n",
    "\n",
    "city_list=get_number_city(city)\n",
    "\n",
    "get_city_ufo_common(city_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 18241 entries, 0 to 18240\n",
      "Data columns (total 6 columns):\n",
      "City               18216 non-null object\n",
      "Colors Reported    2882 non-null object\n",
      "Shape Reported     15597 non-null object\n",
      "State              18241 non-null object\n",
      "Time               18241 non-null object\n",
      "Location           18216 non-null object\n",
      "dtypes: object(6)\n",
      "memory usage: 855.2+ KB\n"
     ]
    }
   ],
   "source": [
    "ufo.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 18241 entries, 0 to 18240\n",
      "Data columns (total 6 columns):\n",
      "City               18216 non-null object\n",
      "Colors Reported    2882 non-null object\n",
      "Shape Reported     15597 non-null object\n",
      "State              18241 non-null object\n",
      "Time               18241 non-null object\n",
      "Location           18216 non-null object\n",
      "dtypes: object(6)\n",
      "memory usage: 855.2+ KB\n"
     ]
    }
   ],
   "source": [
    "ufo.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "ufo.to_csv('ufo.csv',index=False,header=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 18241 entries, 0 to 18240\n",
      "Data columns (total 6 columns):\n",
      "City               18216 non-null object\n",
      "Colors Reported    2882 non-null object\n",
      "Shape Reported     15597 non-null object\n",
      "State              18241 non-null object\n",
      "Time               18241 non-null object\n",
      "Location           18216 non-null object\n",
      "dtypes: object(6)\n",
      "memory usage: 855.2+ KB\n"
     ]
    }
   ],
   "source": [
    "ufo.info()"
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

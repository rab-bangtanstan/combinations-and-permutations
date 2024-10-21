import streamlit as st

from scipy.special import comb,perm


st.title('Event planner 🗓️')

st.write('This app helps you find the combinations and permutations for different events')

st.header('Event1 : Groups formation 👨‍👩‍👧‍👦')

total_people = st.number_input('total number of people: ',min_value = 1,max_value = 100)
group_people = st.number_input('Number of people in group: ',min_value = 1,max_value = 5)

if st.button('Calculate groups: ') == True:

    if total_people >= group_people:
        no_groups = comb(total_people,group_people)
        no_groups = int(no_groups)
        val = 'The total number of groups that can be formed is: '+ str(no_groups)
        st.write(val)

    else:
        st.write('The total number of people have to be greater than or equal to the group number.....')


st.header('Event1 : Keynote speakers arrangement 🎤')

total_speakers = st.number_input('Enter the total number of speakers: ',min_value = 1, max_value = 10)
if st.button('Speaker arrangment : ') == True:
    total_arrangements = int(perm(total_speakers,total_speakers ))
    var = 'total number of ways the speaker can be arranged is: ' + str(total_arrangements)
    st.write(var)


st.header('Event3 : Lottery Pick 🔢')

total_lottery_p = st.number_input('Enter the total number of people signed up for the lottery: ',min_value = 1 ,max_value = 100)

total_won = st.number_input('How many people do you want to win: ',min_value = 1, max_value = 5)
if st.button('Lottery Picker: ') == True:
    total_picked = int(comb(total_lottery_p,total_won))

    var = 'total number of ways in which the winners are picked: ' + str(total_picked)
    st.write(var)


# windows +  .    opens an emoji picker



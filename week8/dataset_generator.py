import csv, random
techincal = ['Bully',
             'Creative',
             'Focused',
             'Goal-oriented',
             'Intelligent',
             'Resourceful',
             'Skilful',
             'Smart',
             'Strategic Planners',
             'Well Trained',
             'Well-networked',
             'Well-organized',
             'Well-trained',
             'Opportunists'
             ]

personal = ['Aggressive',
            'Chaotic state of mind',
            'Coercive',
            'Control freak',
            'Conviction in Violence',
            'Coward',
            'Determined',
            'Emotional',
            'Gullible',
            'Identity crisis',
            'Immoral/ Unethical',
            'Impatient',
            'Incited',
            'Inhuman Psyche',
            'Insensitive',
            'Loner',
            'Passionate',
            'Psychiatric conditions',
            'Psychologically\nDeviant',
            'Risk-taker',
            'Secretive',
            'Selfish',
            'Strong-willed',
            'Vengeful']

social = ['Anti-establishment',
          'Anti-social',
          'Anti-state',
          'Brain-washed',
          'Broken homes/families',
          'Inferiority complex',
          'Insufficient social\nsupport',
          'Intolerance to diversity of opinion',
          'Lack Social skills',
          'Low self-worth',
          'Marginalised',
          'Mass-destruction',
          'Misguided',
          'Need to outsmart others',
          'Radical',
          'Rationalization',
          'Rebellious',
          'Reinforcement available',
          'Social dissatisfaction',
          'Socially inept',
          'Unlawful']

movitating_factor = ['Anger',
                     'Concealed\nexistence',
                     'Curiosity',
                     'Disregard for law',
                     'Emotions',
                     'Enhancing self-\nworth',
                     'Experimentation',
                     'Greed (easy, quick money)',
                     'Intolerance',
                     'Lust',
                     'Manipulate others',
                     'Monetary Gain',
                     'Need to Control others',
                     'No fear of punishment',
                     'Plain boredom',
                     'Political beliefs',
                     'Political support',
                     'Religious\nfundamentalism',
                     'Revenge',
                     'Risk tolerance',
                     'Thrill-seeking']


col_size = len(techincal+personal+social+movitating_factor)
csv_file = open('./data.csv', 'w', newline='')


csv_writer = csv.writer(csv_file, dialect='excel')
csv_writer.writerow(techincal + personal + social + movitating_factor)  # Write headers

'''
We are creating a dateset with one being a criminal and onther not being a criminal
Criminal is one that has higher value in all of above columns
'''

for _ in range(1000):   
    
    if random.randint(0,3) == 0:
        criminal = 1    # might be a criminial
    else:
        criminal = random.random()  # Not a criminal
        
    
    row = [round(random.random(), 5) * criminal for _ in range(col_size)]
    csv_writer.writerow(row)
    csv_file.flush()


csv_file.close()

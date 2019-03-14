#!/usr/bin/env python3

input_first = "out.txt"
input_second = "gold_standard.txt"
output = "evaluation.txt"


def delete_endline(line):
    if line[len(line) - 1] == '\n':
        line = line[0:len(line) - 1]

    return line


with open(input_first, 'r', encoding="utf8") as input_first:
    with open(input_second, 'r', encoding="utf8") as input_second:
        with open(output, 'w', encoding="utf8") as output:

            my_out = input_first.readlines()
            sample_out = input_second.readlines()

            result = 0

            for i in range(len(my_out)):
                my_out[i] = delete_endline(my_out[i])
                sample_out[i] = delete_endline(sample_out[i])

                if my_out[i] != sample_out[i]:
                    feedback = "ERROR on line #" + str(i) + ":\n" \
                               + "out.txt\t\t\t\t" + my_out[i] + "\n" \
                               + "golden_standard.txt\t" + sample_out[i] + "\n\n"
                    output.write(feedback)
                else:
                    result += 1

            final_feedback = "\nTokenization accuracy is equal to " + str(result / len(my_out) * 100) +"% or " + str(result) + "/" + str(len(my_out))
            output.write(final_feedback)
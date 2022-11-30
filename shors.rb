class Shors
    def find_gcd(number_1, number_2)
        return number_1.gcd(number_2)
    end

    def shors_algorithm(number_to_factor)
        if !number_to_factor.is_a? Integer
            return
        end
        N = number_to_factor
        puts "The number is: #{N}"
        K = rand(1..number_to_factor)
        puts "The factor number is #{K}"
        GCD = find_gcd(N, K)
        puts "The GCD is #{GCD}"
        if GCD != 1
            puts "#{GCD} is a factor of #{N}"
        else
            transformations = Array.new()
            q = 1
            iterations = 0
            while true
                q = (q*K) % N
                transformations.push(q)
                iterations += 1
                puts "This iteration #{iterations}, remainder #{q}, N #{N}, and factor #{K}"
                if q == 1
                    break
                end
            end
            if iterations % 2 != 0
                puts "Number of iterations is not even"
                shors_algorithm(N)
            else
                p = transformations[int((iterations/2)-1)]
                puts "This is p #{p}"
                if p + 1 == N
                    puts "P + 1 == N, recalling function"
                    shors_algorithm(N)
                else
                    puts "This is the #{int(iterations/2)} transformation"
                    puts "#{find_gcd(p+1, N)} and #{find_gcd(p-1, N)} are factors of #{N}"
                end
            end
        end
    end
end

shors = Shors.new()
shors.shors_algorithm(gets.chomp.to_i)
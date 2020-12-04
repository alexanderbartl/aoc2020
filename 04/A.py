with open('input.txt') as f:
    raw_passports = f.read().split('\n\n')

required_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
print(sum([int(all([field in passport for field in required_fields])) for passport in raw_passports]))

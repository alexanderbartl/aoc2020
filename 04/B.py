import re


with open('input.txt') as f:
    raw_passports = f.read().split('\n\n')


def validate(passport):
    try:
        if not (1920 <= int(passport['byr']) <= 2002):
            print('invalid byr', passport['byr'])
            return False
        if not (2010 <= int(passport['iyr']) <= 2020):
            print('invalid iyr', passport['iyr'])
            return False
        if not (2020 <= int(passport['eyr']) <= 2030):
            print('invalid eyr', passport['eyr'])
            return False
        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            print('invalid ecl', passport['ecl'])
            return False
        if not re.match('^\d{9}$', passport['pid']):
            print('invalid pid', passport['pid'])
            return False
        if not re.match('^#[0-9a-f]{6}$', passport['hcl']):
            print('invalid hcl', passport['hcl'])
            return False
        if not re.match('^\d{2,3}(cm|in)$', passport['hgt']):
            print('invalid hgt', passport['hgt'])
            return False
        if passport['hgt'][-2:] == 'in':
            return 59 <= int(passport['hgt'].replace('in', '')) <= 76
        else:
            return 150 <= int(passport['hgt'].replace('cm', '')) <= 193
    except Exception as e:
        print(e)
        return False


valid = 0
for raw_passport in raw_passports:
    fields = [field.split(':') for field in raw_passport.split()]
    passport = dict(fields)
    valid += int(validate(passport))
print(valid)

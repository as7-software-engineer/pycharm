'''tipos de erro/excessão
print(x) erro de nome; int(input) = oito erro de valor;
divisões por zero. zero division error
r=2/'2' typeerror erro de tipos excessão
erro de index ou keyerror
import uteis
moduleNotFoundError
python ( NameError; ValueError; ZeroDivisionError; TypeError; IndexError; KeyError;EOFError;KeyboardInterrupt;OSError;
MemoryError;ConnectionError; RunTimeError
toda excessão em python é filho de uma classe maior, Exception
-----------------------------------------------------------------------------
try:
    operação

except:
    falhou
'''
# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     print(f'Problema encontrado é {erro.__class__}')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito obrigado!')

''' cada erro tem uma excessão
try:
    operação

except TypeError:
    falhou
    
except ValueError:
    falhou
    
except OSEError:
    falhou    

finally:
    certo/falha
'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')


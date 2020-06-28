from .games.mines import MineBoard
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def mine(request):
    brd = MineBoard(10, 14)
    # request.session['brd'] = brd
    request.session['brd'] = brd.__dict__
    # print(request.session.session_key)
    return render(request, 'game/mine.html')

def search_mine(request,y,x):
    # print(y,x)
    brd = MineBoard(dic=request.session.get('brd'))
    if brd.firstsearch(y, x):
        result = True
    else:
        brd.search_board(y, x)
        result = False
    context = {
        'board' : brd.findedbrd,
        'result' : result,
        'clear' : False,
        'flag' : len(brd.flag),
    }
    print(brd.flag)
    request.session['brd'] = brd.__dict__
    return JsonResponse(context)

def flag_evnet(request,y,x):
    brd = MineBoard(dic=request.session.get('brd'))
    result = brd.check_flag(y, x)
    context = {
        'board' : brd.findedbrd,
        'result' : result,
        'clear' : True,
        'flag' : len(brd.flag),
    }
    request.session['brd'] = brd.__dict__
    return JsonResponse(context)
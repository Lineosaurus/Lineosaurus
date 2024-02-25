import os, sys
sys.path.append(os.environ['GITHUB_ACTION_PATH'])  # make the needed folders importable
from lino_core.engine.gather_stuff import gather_stuff
from lino_core.engine.update_readme import update_readme

def main():
    
    ipts = {  # inputs
        'nickname': os.environ['IPT__nickname'],
        'banner': os.environ['IPT__banner'] if (os.environ['IPT__banner'] != '') else None,
        'include_last_activity': True if (os.environ['IPT__include_last_activity'] == 'true') else False,
        'credit': True if (os.environ['IPT__credit'] == 'true') else False,
    }
    for k,v in ipts.items(): print(f"DEBUG: (inputs) {k}: {repr(v)}")

    misc = {  # various constants
        'root_user': os.environ['GITHUB_WORKSPACE'],
        'root_action': os.environ['GITHUB_ACTION_PATH'],
        'gh_actor': os.environ['GITHUB_ACTOR'],
        'act_ver': os.environ['ACTION_REF'],  # the Action version
    }
    for k,v in misc.items(): print(f"DEBUG: (misc constants) {k}: {repr(v)}")

    needed = gather_stuff(
        root_user=misc['root_user'],
        gh_actor=misc['gh_actor'],
    )
    update_readme(
        banner_pth=ipts['banner'],
        gh_actor=misc['gh_actor'],
        
        lines_of_code=needed['lines_of_code'],
        nChars=needed['nChars'],
        
        include_last_activity=ipts['include_last_activity'],
        last_act=needed['last_act'],
        
        nickname=ipts['nickname'],
        nCommits_last_week=needed['nCommits_last_week'],
        lino_ver=misc['act_ver'],
        readme_pth=os.path.join(misc['root_user'], 'README.md'),
        include_credit=ipts['credit'],
    )

if __name__ == '__main__':
    main()

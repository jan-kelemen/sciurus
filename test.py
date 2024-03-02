#!/usr/bin/python3

import argparse
import glob
import pathlib
import os
import shutil
import subprocess
import sys

tiny_tests = [
        "test10", 
        "test20", 
        "test21",
        "test22",
        "test23",
        "test24",
        "test25",
        "test26",
        "test27"
]

new_tests = [
        "test_arabic",
        "test_arglist",
        "test_assert",
        "test_autochdir",
        "test_autocmd",
        "test_autoload",
        "test_backspace_opt",
        "test_backup",
        "test_balloon",
        "test_balloon_gui",
        "test_behave",
        "test_blob",
        "test_blockedit",
        "test_breakindent",
        "test_buffer",
        "test_bufline",
        "test_bufwintabinfo",
        "test_cd",
        "test_cdo",
        "test_changedtick",
        "test_changelist",
        "test_channel",
        "test_charsearch",
        "test_charsearch_utf8",
        "test_checkpath",
        "test_cindent",
        "test_cjk_linebreak",
        "test_clientserver",
        "test_close_count",
        "test_cmd_lists",
        "test_cmdline",
        "test_cmdmods",
        "test_cmdwin",
        "test_codestyle",
        "test_command_count",
        "test_comments",
        "test_comparators",
        "test_compiler",
        "test_conceal",
        "test_const",
        "test_cpoptions",
        "test_crash",
        "test_crypt",
        "test_cscope",
        "test_cursor_func",
        "test_cursorline",
        "test_curswant",
        "test_debugger",
        "test_delete",
        "test_diffmode",
        "test_digraph",
        "test_display",
        "test_edit",
        "test_environ",
        "test_erasebackword",
        "test_escaped_glob",
        "test_eval_stuff",
        "test_ex_equal",
        "test_ex_mode",
        "test_ex_undo",
        "test_ex_z",
        "test_excmd",
        "test_exec_while_if",
        "test_execute_func",
        "test_exists",
        "test_exists_autocmd",
        "test_exit",
        "test_expand",
        "test_expand_dllpath",
        "test_expand_func",
        "test_expr",
        "test_expr_utf8",
        "test_file_perm",
        "test_file_size",
        "test_filechanged",
        "test_fileformat",
        "test_filetype",
        "test_filter_cmd",
        "test_filter_map",
        "test_find_complete",
        "test_findfile",
        "test_fixeol",
        "test_flatten",
        "test_float_func",
        "test_fnameescape",
        "test_fnamemodify",
        "test_fold",
        "test_format",
        "test_functions",
        "test_function_lists",
        "test_ga",
        "test_getcwd",
        "test_getvar",
        "test_gf",
        "test_glob2regpat",
        "test_global",
        "test_gn",
        "test_goto",
        "test_gui",
        "test_gui_init",
        "test_hardcopy",
        "test_help",
        "test_help_tagjump",
        "test_hide",
        "test_highlight",
        "test_history",
        "test_hlsearch",
        "test_iminsert",
        "test_increment",
        "test_increment_dbcs",
        "test_indent",
        "test_input",
        "test_ins_complete",
        "test_ins_complete_no_halt",
        "test_interrupt",
        "test_job_fails",
        "test_join",
        "test_json",
        "test_jumplist",
        "test_lambda",
        "test_langmap",
        "test_largefile",
        "test_let",
        "test_lineending",
        "test_lispindent",
        "test_listchars",
        "test_listdict",
        "test_listener",
        "test_listlbr",
        "test_listlbr_utf8",
        "test_lua",
        "test_makeencoding",
        "test_man",
        "test_map_functions",
        "test_mapping",
        "test_marks",
        "test_match",
        "test_matchadd_conceal",
        "test_matchadd_conceal_utf8",
        "test_matchfuzzy",
        "test_matchparen",
        "test_memory_usage",
        "test_menu",
        "test_messages",
        "test_method",
        "test_mksession",
        "test_mksession_utf8",
        "test_modeless",
        "test_modeline",
        "test_move",
        "test_mswin_event",
        "test_mzscheme",
        "test_nested_function",
        "test_netbeans",
        "test_normal",
        "test_number",
        "test_options",
        "test_packadd",
        "test_partial",
        "test_paste",
        "test_perl",
        "test_plus_arg_edit",
        "test_popup",
        "test_popupwin",
        "test_popupwin_textprop",
        "test_preview",
        "test_profile",
        "test_prompt_buffer",
        "test_put",
        "test_python2",
        "test_python3",
        "test_pyx2",
        "test_pyx3",
        "test_quickfix",
        "test_quotestar",
        "test_random",
        "test_recover",
        "test_regex_char_classes",
        "test_regexp_latin",
        "test_regexp_utf8",
        "test_registers",
        "test_reltime",
        "test_remote",
        "test_rename",
        "test_restricted",
        "test_retab",
        "test_ruby",
        "test_scriptnames",
        "test_scroll_opt",
        "test_scrollbind",
        "test_search",
        "test_search_stat",
        "test_searchpos",
        "test_selectmode",
        "test_set",
        "test_sha256",
        "test_shell",
        "test_shift",
        "test_shortpathname",
        "test_signals",
        "test_signs",
        "test_sleep",
        "test_smartindent",
        "test_sort",
        "test_sound",
        "test_source",
        "test_source_utf8",
        "test_spell",
        "test_spell_utf8",
        "test_spellfile",
        "test_startup",
        "test_startup_utf8",
        "test_stat",
        "test_statusline",
        "test_substitute",
        "test_suspend",
        "test_swap",
        "test_syn_attr",
        "test_syntax",
        "test_system",
        "test_tab",
        "test_tabline",
        "test_tabpage",
        "test_tagcase",
        "test_tagfunc",
        "test_tagjump",
        "test_taglist",
        "test_tcl",
        "test_termcodes",
        "test_termdebug",
        "test_termencoding",
        "test_terminal",
        "test_terminal2",
        "test_terminal3",
        "test_terminal_fail",
        "test_textformat",
        "test_textobjects",
        "test_textprop",
        "test_timers",
        "test_true_false",
        "test_trycatch",
        "test_undo",
        "test_unlet",
        "test_user_func",
        "test_usercommands",
        "test_utf8",
        "test_utf8_comparisons",
        "test_vartabs",
        "test_version",
        "test_vim9_assign",
        "test_vim9_builtin",
        "test_vim9_class",
        "test_vim9_cmd",
        "test_vim9_disassemble",
        "test_vim9_expr",
        "test_vim9_fails",
        "test_vim9_func",
        "test_vim9_import",
        "test_vim9_script",
        "test_vim9_typealias",
        "test_viminfo",
        "test_vimscript",
        "test_virtualedit",
        "test_visual",
        "test_winbar",
        "test_winbuf_close",
        "test_window_cmd",
        "test_window_id",
        "test_windows_home",
        "test_wnext",
        "test_wordcount",
        "test_writefile",
        "test_xxd",
        "test_alot_latin",
        "test_alot_utf8",
        "test_alot"
]

def nolog(working_directory):
    for path in ["test_result.log", "test.log", "messages", "starttime"]:
        try:
            os.remove(os.path.join(working_directory, path))
        except:
            pass

def report(working_directory):
    test_log = os.path.join(working_directory, "test.log")
    result_log = os.path.join(working_directory, "test_result.log")

    if os.path.exists(test_log):
        shutil.copyfile(test_log, result_log)
    else:
        with open(result_log, "a") as log:
            log.write("No failures reported\n")

    run_result = subprocess.run(
            [vim_name, "-u", "NONE", "--noplugin", "--not-a-term",
             "-S", "summarize.vim", "messages",
             "--cmd", """au SwapExists * let v:swapchoice = "e" """], cwd=working_directory, stdout=subprocess.DEVNULL)

    try:
        os.remove(working_directory, "starttime")
    except:
        pass

    print("\nTest results:\n")
    with open(result_log, "r") as f:
        shutil.copyfileobj(f, sys.stdout)

    if os.path.exists(test_log):
        print("TEST FAILURE\n")
        exit(1)
    else:
        print("ALL DONE\n")

def tinytests(vim_name, working_directory):
    for test in tiny_tests:
        run_result = subprocess.run(
                [vim_name, "-u", "unix.vim",
                 "-U", "NONE", "--noplugin",  "--not-a-term",
                 "-s", "dotest.in",
                 "{}.in".format(test),
                 "--cmd", """au SwapExists * let v:swapchoice = "e" """], cwd=working_directory, stdout=subprocess.DEVNULL)

        if run_result.returncode != 0:
            print(f"{test} exited with code: {run_result.returncode}")

        output_file = os.path.join(working_directory, "test.out")
        log_file = os.path.join(working_directory, "test.log")

        if os.path.exists(output_file):
            diff_result = subprocess.run(
                    ["diff", "test.out", f"{test}.ok"], cwd=working_directory)

            if diff_result.returncode > 0:
                with open(log_file, "a") as log:
                    log.write(f"{test} FAILED\n")
                os.rename(output_file, os.path.join(working_directory, f"{test}.failed"))
            else:
                os.rename(output_file, os.path.join(working_directory, f"{test}.ok"))

        else:
            with open(log_file, "a") as log:
                log.write(f"{test} NO OUTPUT\n")

        for path in glob.glob(os.path.join(working_directory, "X*")):
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)

        try:
            os.remove(os.path.join(working_directory, "viminfo"))
        except:
            pass

def newtests(vim_name, working_directory, runtime, xxd_name):
    for test in new_tests:
        output = subprocess.DEVNULL
        if test in []: # Add test which for which output should be forwarded to stdout
            output = None

        #Test_visual_block_scroll - something is off with the colors
        #Test_xxd_color2 - dump contains relative path to vimruntime which is changed in this tests
        #Test_disassemble_closure_in_loop - for some reason an additional blank line is entered at beginning when TEST_MAY_FAIL variable is defined
        extra_env = {
                "TEST_MAY_FAIL":"Test_visual_block_scroll,Test_xxd_color2,Test_disassemble_closure_in_loop"
                }
        if test in ["test_xxd"]:
            extra_env["XXD"] = xxd_name

        vimcmd = os.path.join(working_directory, "vimcmd")
        with open(vimcmd, "a") as cmd:
            cmd.write(f"{vim_name}\n")
            cmd.write(f"VIMRUNTIME={runtime} {vim_name} -f -u unix.vim --gui-dialog-file guidialog")

        print(test)
        run_result = subprocess.run(
                [vim_name, "-f", "-u", "unix.vim", "--gui-dialog-file", "guidialog",
                 "-U", "NONE", "--noplugin",  "--not-a-term",
                 "-S", "runtest.vim", 
                 f"{test}.vim", "--cmd", """au SwapExists * let v:swapchoice = "e" """], 
                cwd=working_directory, 
                env={**os.environ, "TERM":"xterm", "DEBIAN_FRONTEND":"noninteractive", "VIMRUNTIME":runtime, "DISPLAY":":99", **extra_env},
                stdout=output)

        os.remove(vimcmd)

        if run_result.returncode != 0:
            print(f"{test} exited with code: {run_result.returncode}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--vim-name", default="base/src/vim")
    parser.add_argument("--working-directory", default="base/src/testdir")
    parser.add_argument("--runtime", default="base/runtime")
    parser.add_argument("--xxd-name", default="base/src/xxd/xxd")

    args = parser.parse_args()

    vim_name = os.path.abspath(args.vim_name)
    working_directory = os.path.abspath(args.working_directory)
    runtime = os.path.abspath(args.runtime)
    xxd_name = os.path.abspath(args.xxd_name)
    print(f"Using vim: '{vim_name}'")
    print(f"Using working directory: '{working_directory}'")
    print(f"Using runtime: '{runtime}'")
    print(f"Using xxd: '{xxd_name}")

    nolog(working_directory)
    tinytests(vim_name, working_directory)
    newtests(vim_name, working_directory, runtime, xxd_name)
    report(working_directory)


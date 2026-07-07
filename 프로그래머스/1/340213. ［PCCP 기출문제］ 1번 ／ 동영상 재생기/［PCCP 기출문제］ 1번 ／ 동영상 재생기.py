def solution(video_len, pos, op_start, op_end, commands):
    video_len = int(video_len.replace(':', ''))
    pos = int(pos.replace(':', ''))
    op_start = int(op_start.replace(':', ''))
    op_end = int(op_end.replace(':', ''))
    
    if op_start <= pos < op_end:
        pos = op_end
    for c in commands:
        if c == 'next':
            if pos%100 >= 50:
                pos = (pos//100 + 1)*100 + (pos%100 - 60)
            pos = min(video_len, pos+10)
        elif c == 'prev':
            if pos%100 < 10:
                pos = (pos//100 - 1)*100 + (pos%100 + 60)
            pos = max(0, pos-10)
        if op_start <= pos < op_end:
            pos = op_end
        
    pos = str(pos).zfill(4)
    return pos[:2]+':'+pos[2:]
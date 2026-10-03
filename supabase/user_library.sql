-- Last-write-wins reading progress and bookmark sync.
-- Run once in the Supabase SQL editor for this project.

create table if not exists public.user_library (
  user_id uuid primary key references auth.users (id) on delete cascade,
  progress jsonb,
  progress_updated_at timestamptz,
  bookmarks jsonb not null default '[]'::jsonb,
  tombstones jsonb not null default '{}'::jsonb,
  bookmarks_updated_at timestamptz
);

alter table public.user_library enable row level security;

drop policy if exists "user_library_select_own" on public.user_library;
drop policy if exists "user_library_insert_own" on public.user_library;
drop policy if exists "user_library_update_own" on public.user_library;

create policy "user_library_select_own"
  on public.user_library
  for select
  using (auth.uid() = user_id);

create policy "user_library_insert_own"
  on public.user_library
  for insert
  with check (auth.uid() = user_id);

create policy "user_library_update_own"
  on public.user_library
  for update
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

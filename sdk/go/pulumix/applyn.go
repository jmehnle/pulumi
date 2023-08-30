// Copyright 2016-2023, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by gen-pux-applyn; DO NOT EDIT.

//nolint:lll
package pulumix

import "context"

// ApplyContextErr applies a function to an input,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
func ApplyContextErr[A1, B any](
	ctx context.Context,
	i1 Input[A1],
	fn func(A1) (B, error),
) Output[B] {
	return Compose[B](ctx, func(c *Composer) (B, error) {
		return fn(
			ComposeAwait[A1](c, i1),
		)
	})
}

// ApplyContext applies a function to an input,
// returning an Output holding the result of the function.
//
// This is a variant of ApplyContextErr
// that does not allow the function to return an error.
func ApplyContext[A1, B any](
	ctx context.Context,
	i1 Input[A1],
	fn func(A1) B,
) Output[B] {
	return ApplyContextErr(
		ctx,
		i1,
		func(a1 A1) (B, error) {
			return fn(a1), nil
		},
	)
}

// ApplyErr applies a function to an input,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
//
// This is a variant of ApplyContextErr
// that uses the background context.
func ApplyErr[A1, B any](
	i1 Input[A1],
	fn func(A1) (B, error),
) Output[B] {
	ctx := context.Background()
	return ApplyContextErr(ctx, i1, fn)
}

// Apply applies a function to an input,
// returning an Output holding the result of the function.
//
// This is a variant of ApplyContextErr
// that does not allow the function to return an error,
// and uses the background context.
func Apply[A1, B any](
	i1 Input[A1],
	fn func(A1) B,
) Output[B] {
	ctx := context.Background()
	return ApplyContext(ctx, i1, fn)
}

// Apply2ContextErr applies a function to 2 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
func Apply2ContextErr[A1, A2, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2],
	fn func(A1, A2) (B, error),
) Output[B] {
	return Compose[B](ctx, func(c *Composer) (B, error) {
		return fn(
			ComposeAwait[A1](c, i1),
			ComposeAwait[A2](c, i2),
		)
	})
}

// Apply2Context applies a function to 2 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply2ContextErr
// that does not allow the function to return an error.
func Apply2Context[A1, A2, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2],
	fn func(A1, A2) B,
) Output[B] {
	return Apply2ContextErr(
		ctx,
		i1, i2,
		func(a1 A1, a2 A2) (B, error) {
			return fn(a1, a2), nil
		},
	)
}

// Apply2Err applies a function to 2 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
//
// This is a variant of Apply2ContextErr
// that uses the background context.
func Apply2Err[A1, A2, B any](
	i1 Input[A1], i2 Input[A2],
	fn func(A1, A2) (B, error),
) Output[B] {
	ctx := context.Background()
	return Apply2ContextErr(ctx, i1, i2, fn)
}

// Apply2 applies a function to 2 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply2ContextErr
// that does not allow the function to return an error,
// and uses the background context.
func Apply2[A1, A2, B any](
	i1 Input[A1], i2 Input[A2],
	fn func(A1, A2) B,
) Output[B] {
	ctx := context.Background()
	return Apply2Context(ctx, i1, i2, fn)
}

// Apply3ContextErr applies a function to 3 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
func Apply3ContextErr[A1, A2, A3, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3],
	fn func(A1, A2, A3) (B, error),
) Output[B] {
	return Compose[B](ctx, func(c *Composer) (B, error) {
		return fn(
			ComposeAwait[A1](c, i1),
			ComposeAwait[A2](c, i2),
			ComposeAwait[A3](c, i3),
		)
	})
}

// Apply3Context applies a function to 3 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply3ContextErr
// that does not allow the function to return an error.
func Apply3Context[A1, A2, A3, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3],
	fn func(A1, A2, A3) B,
) Output[B] {
	return Apply3ContextErr(
		ctx,
		i1, i2, i3,
		func(a1 A1, a2 A2, a3 A3) (B, error) {
			return fn(a1, a2, a3), nil
		},
	)
}

// Apply3Err applies a function to 3 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
//
// This is a variant of Apply3ContextErr
// that uses the background context.
func Apply3Err[A1, A2, A3, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3],
	fn func(A1, A2, A3) (B, error),
) Output[B] {
	ctx := context.Background()
	return Apply3ContextErr(ctx, i1, i2, i3, fn)
}

// Apply3 applies a function to 3 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply3ContextErr
// that does not allow the function to return an error,
// and uses the background context.
func Apply3[A1, A2, A3, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3],
	fn func(A1, A2, A3) B,
) Output[B] {
	ctx := context.Background()
	return Apply3Context(ctx, i1, i2, i3, fn)
}

// Apply4ContextErr applies a function to 4 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
func Apply4ContextErr[A1, A2, A3, A4, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4],
	fn func(A1, A2, A3, A4) (B, error),
) Output[B] {
	return Compose[B](ctx, func(c *Composer) (B, error) {
		return fn(
			ComposeAwait[A1](c, i1),
			ComposeAwait[A2](c, i2),
			ComposeAwait[A3](c, i3),
			ComposeAwait[A4](c, i4),
		)
	})
}

// Apply4Context applies a function to 4 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply4ContextErr
// that does not allow the function to return an error.
func Apply4Context[A1, A2, A3, A4, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4],
	fn func(A1, A2, A3, A4) B,
) Output[B] {
	return Apply4ContextErr(
		ctx,
		i1, i2, i3, i4,
		func(a1 A1, a2 A2, a3 A3, a4 A4) (B, error) {
			return fn(a1, a2, a3, a4), nil
		},
	)
}

// Apply4Err applies a function to 4 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
//
// This is a variant of Apply4ContextErr
// that uses the background context.
func Apply4Err[A1, A2, A3, A4, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4],
	fn func(A1, A2, A3, A4) (B, error),
) Output[B] {
	ctx := context.Background()
	return Apply4ContextErr(ctx, i1, i2, i3, i4, fn)
}

// Apply4 applies a function to 4 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply4ContextErr
// that does not allow the function to return an error,
// and uses the background context.
func Apply4[A1, A2, A3, A4, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4],
	fn func(A1, A2, A3, A4) B,
) Output[B] {
	ctx := context.Background()
	return Apply4Context(ctx, i1, i2, i3, i4, fn)
}

// Apply5ContextErr applies a function to 5 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
func Apply5ContextErr[A1, A2, A3, A4, A5, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5],
	fn func(A1, A2, A3, A4, A5) (B, error),
) Output[B] {
	return Compose[B](ctx, func(c *Composer) (B, error) {
		return fn(
			ComposeAwait[A1](c, i1),
			ComposeAwait[A2](c, i2),
			ComposeAwait[A3](c, i3),
			ComposeAwait[A4](c, i4),
			ComposeAwait[A5](c, i5),
		)
	})
}

// Apply5Context applies a function to 5 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply5ContextErr
// that does not allow the function to return an error.
func Apply5Context[A1, A2, A3, A4, A5, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5],
	fn func(A1, A2, A3, A4, A5) B,
) Output[B] {
	return Apply5ContextErr(
		ctx,
		i1, i2, i3, i4, i5,
		func(a1 A1, a2 A2, a3 A3, a4 A4, a5 A5) (B, error) {
			return fn(a1, a2, a3, a4, a5), nil
		},
	)
}

// Apply5Err applies a function to 5 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
//
// This is a variant of Apply5ContextErr
// that uses the background context.
func Apply5Err[A1, A2, A3, A4, A5, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5],
	fn func(A1, A2, A3, A4, A5) (B, error),
) Output[B] {
	ctx := context.Background()
	return Apply5ContextErr(ctx, i1, i2, i3, i4, i5, fn)
}

// Apply5 applies a function to 5 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply5ContextErr
// that does not allow the function to return an error,
// and uses the background context.
func Apply5[A1, A2, A3, A4, A5, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5],
	fn func(A1, A2, A3, A4, A5) B,
) Output[B] {
	ctx := context.Background()
	return Apply5Context(ctx, i1, i2, i3, i4, i5, fn)
}

// Apply6ContextErr applies a function to 6 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
func Apply6ContextErr[A1, A2, A3, A4, A5, A6, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6],
	fn func(A1, A2, A3, A4, A5, A6) (B, error),
) Output[B] {
	return Compose[B](ctx, func(c *Composer) (B, error) {
		return fn(
			ComposeAwait[A1](c, i1),
			ComposeAwait[A2](c, i2),
			ComposeAwait[A3](c, i3),
			ComposeAwait[A4](c, i4),
			ComposeAwait[A5](c, i5),
			ComposeAwait[A6](c, i6),
		)
	})
}

// Apply6Context applies a function to 6 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply6ContextErr
// that does not allow the function to return an error.
func Apply6Context[A1, A2, A3, A4, A5, A6, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6],
	fn func(A1, A2, A3, A4, A5, A6) B,
) Output[B] {
	return Apply6ContextErr(
		ctx,
		i1, i2, i3, i4, i5, i6,
		func(a1 A1, a2 A2, a3 A3, a4 A4, a5 A5, a6 A6) (B, error) {
			return fn(a1, a2, a3, a4, a5, a6), nil
		},
	)
}

// Apply6Err applies a function to 6 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
//
// This is a variant of Apply6ContextErr
// that uses the background context.
func Apply6Err[A1, A2, A3, A4, A5, A6, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6],
	fn func(A1, A2, A3, A4, A5, A6) (B, error),
) Output[B] {
	ctx := context.Background()
	return Apply6ContextErr(ctx, i1, i2, i3, i4, i5, i6, fn)
}

// Apply6 applies a function to 6 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply6ContextErr
// that does not allow the function to return an error,
// and uses the background context.
func Apply6[A1, A2, A3, A4, A5, A6, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6],
	fn func(A1, A2, A3, A4, A5, A6) B,
) Output[B] {
	ctx := context.Background()
	return Apply6Context(ctx, i1, i2, i3, i4, i5, i6, fn)
}

// Apply7ContextErr applies a function to 7 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
func Apply7ContextErr[A1, A2, A3, A4, A5, A6, A7, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6], i7 Input[A7],
	fn func(A1, A2, A3, A4, A5, A6, A7) (B, error),
) Output[B] {
	return Compose[B](ctx, func(c *Composer) (B, error) {
		return fn(
			ComposeAwait[A1](c, i1),
			ComposeAwait[A2](c, i2),
			ComposeAwait[A3](c, i3),
			ComposeAwait[A4](c, i4),
			ComposeAwait[A5](c, i5),
			ComposeAwait[A6](c, i6),
			ComposeAwait[A7](c, i7),
		)
	})
}

// Apply7Context applies a function to 7 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply7ContextErr
// that does not allow the function to return an error.
func Apply7Context[A1, A2, A3, A4, A5, A6, A7, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6], i7 Input[A7],
	fn func(A1, A2, A3, A4, A5, A6, A7) B,
) Output[B] {
	return Apply7ContextErr(
		ctx,
		i1, i2, i3, i4, i5, i6, i7,
		func(a1 A1, a2 A2, a3 A3, a4 A4, a5 A5, a6 A6, a7 A7) (B, error) {
			return fn(a1, a2, a3, a4, a5, a6, a7), nil
		},
	)
}

// Apply7Err applies a function to 7 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
//
// This is a variant of Apply7ContextErr
// that uses the background context.
func Apply7Err[A1, A2, A3, A4, A5, A6, A7, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6], i7 Input[A7],
	fn func(A1, A2, A3, A4, A5, A6, A7) (B, error),
) Output[B] {
	ctx := context.Background()
	return Apply7ContextErr(ctx, i1, i2, i3, i4, i5, i6, i7, fn)
}

// Apply7 applies a function to 7 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply7ContextErr
// that does not allow the function to return an error,
// and uses the background context.
func Apply7[A1, A2, A3, A4, A5, A6, A7, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6], i7 Input[A7],
	fn func(A1, A2, A3, A4, A5, A6, A7) B,
) Output[B] {
	ctx := context.Background()
	return Apply7Context(ctx, i1, i2, i3, i4, i5, i6, i7, fn)
}

// Apply8ContextErr applies a function to 8 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
func Apply8ContextErr[A1, A2, A3, A4, A5, A6, A7, A8, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6], i7 Input[A7], i8 Input[A8],
	fn func(A1, A2, A3, A4, A5, A6, A7, A8) (B, error),
) Output[B] {
	return Compose[B](ctx, func(c *Composer) (B, error) {
		return fn(
			ComposeAwait[A1](c, i1),
			ComposeAwait[A2](c, i2),
			ComposeAwait[A3](c, i3),
			ComposeAwait[A4](c, i4),
			ComposeAwait[A5](c, i5),
			ComposeAwait[A6](c, i6),
			ComposeAwait[A7](c, i7),
			ComposeAwait[A8](c, i8),
		)
	})
}

// Apply8Context applies a function to 8 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply8ContextErr
// that does not allow the function to return an error.
func Apply8Context[A1, A2, A3, A4, A5, A6, A7, A8, B any](
	ctx context.Context,
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6], i7 Input[A7], i8 Input[A8],
	fn func(A1, A2, A3, A4, A5, A6, A7, A8) B,
) Output[B] {
	return Apply8ContextErr(
		ctx,
		i1, i2, i3, i4, i5, i6, i7, i8,
		func(a1 A1, a2 A2, a3 A3, a4 A4, a5 A5, a6 A6, a7 A7, a8 A8) (B, error) {
			return fn(a1, a2, a3, a4, a5, a6, a7, a8), nil
		},
	)
}

// Apply8Err applies a function to 8 inputs,
// returning an Output holding the result of the function.
//
// If the function returns an error, the Output will be in an error state.
//
// This is a variant of Apply8ContextErr
// that uses the background context.
func Apply8Err[A1, A2, A3, A4, A5, A6, A7, A8, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6], i7 Input[A7], i8 Input[A8],
	fn func(A1, A2, A3, A4, A5, A6, A7, A8) (B, error),
) Output[B] {
	ctx := context.Background()
	return Apply8ContextErr(ctx, i1, i2, i3, i4, i5, i6, i7, i8, fn)
}

// Apply8 applies a function to 8 inputs,
// returning an Output holding the result of the function.
//
// This is a variant of Apply8ContextErr
// that does not allow the function to return an error,
// and uses the background context.
func Apply8[A1, A2, A3, A4, A5, A6, A7, A8, B any](
	i1 Input[A1], i2 Input[A2], i3 Input[A3], i4 Input[A4], i5 Input[A5], i6 Input[A6], i7 Input[A7], i8 Input[A8],
	fn func(A1, A2, A3, A4, A5, A6, A7, A8) B,
) Output[B] {
	ctx := context.Background()
	return Apply8Context(ctx, i1, i2, i3, i4, i5, i6, i7, i8, fn)
}

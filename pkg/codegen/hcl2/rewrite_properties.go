package hcl2

import (
	"bytes"
	"fmt"

	"github.com/hashicorp/hcl/v2"
	"github.com/pulumi/pulumi/pkg/v2/codegen/hcl2/model"
	"github.com/pulumi/pulumi/sdk/v2/go/common/util/contract"
	"github.com/zclconf/go-cty/cty"
)

func RewritePropertyReferences(expr model.Expression) model.Expression {
	rewriter := func(expr model.Expression) (model.Expression, hcl.Diagnostics) {
		traversal, ok := expr.(*model.ScopeTraversalExpression)
		if !ok {
			return expr, nil
		}

		p, ok := traversal.Parts[len(traversal.Parts)-1].(*ResourceProperty)
		if !ok {
			return expr, nil
		}

		var buffer bytes.Buffer
		for _, t := range p.Path {
			var err error
			switch t := t.(type) {
			case hcl.TraverseRoot:
				_, err = fmt.Fprint(&buffer, t.Name)
			case hcl.TraverseAttr:
				_, err = fmt.Fprintf(&buffer, ".%s", t.Name)
			case hcl.TraverseIndex:
				switch t.Key.Type() {
				case cty.String:
					_, err = fmt.Fprintf(&buffer, ".%s", t.Key.AsString())
				case cty.Number:
					idx, _ := t.Key.AsBigFloat().Int64()
					_, err = fmt.Fprintf(&buffer, "[%d]", idx)
				default:
					contract.Failf("unexpected traversal index of type %v", t.Key.Type())
				}
			}
			contract.IgnoreError(err)
		}

		// TODO: transfer internal trivia

		propertyPath := buffer.String()
		value := model.NewQuotedStringLiteral(propertyPath)
		value.SetLeadingTrivia(expr.GetLeadingTrivia())
		value.SetTrailingTrivia(expr.GetTrailingTrivia())
		diags := value.Typecheck(false)
		contract.Assert(len(diags) == 0)
		return value, nil
	}

	expr, diags := model.VisitExpression(expr, model.IdentityVisitor, rewriter)
	contract.Assert(len(diags) == 0)
	return expr
}

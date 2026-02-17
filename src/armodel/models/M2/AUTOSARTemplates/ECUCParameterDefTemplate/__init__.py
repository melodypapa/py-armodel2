"""ECUCParameterDefTemplate module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
        EcucModuleDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_collection import (
        EcucDefinitionCollection,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
        EcucContainerDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_param_conf_container_def import (
        EcucParamConfContainerDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_choice_container_def import (
        EcucChoiceContainerDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
        EcucDefinitionElement,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
        EcucCommonAttributes,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_configuration_class import (
        EcucAbstractConfigurationClass,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_value_configuration_class import (
        EcucValueConfigurationClass,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_multiplicity_configuration_class import (
        EcucMultiplicityConfigurationClass,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
        EcucParameterDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_boolean_param_def import (
        EcucBooleanParamDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_integer_param_def import (
        EcucIntegerParamDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_float_param_def import (
        EcucFloatParamDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_string_param_def import (
        EcucAbstractStringParamDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_string_param_def import (
        EcucStringParamDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_multiline_string_param_def import (
        EcucMultilineStringParamDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_linker_symbol_def import (
        EcucLinkerSymbolDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_function_name_def import (
        EcucFunctionNameDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_enumeration_param_def import (
        EcucEnumerationParamDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_enumeration_literal_def import (
        EcucEnumerationLiteralDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_add_info_param_def import (
        EcucAddInfoParamDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_reference_def import (
        EcucAbstractReferenceDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
        EcucAbstractInternalReferenceDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_external_reference_def import (
        EcucAbstractExternalReferenceDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_reference_def import (
        EcucReferenceDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_choice_reference_def import (
        EcucChoiceReferenceDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_foreign_reference_def import (
        EcucForeignReferenceDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_instance_reference_def import (
        EcucInstanceReferenceDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_uri_reference_def import (
        EcucUriReferenceDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def_set import (
        EcucDestinationUriDefSet,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
        EcucDestinationUriDef,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_policy import (
        EcucDestinationUriPolicy,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_derivation_specification import (
        EcucDerivationSpecification,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_derivation_formula import (
        EcucParameterDerivationFormula,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
        EcucQuery,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query_expression import (
        EcucQueryExpression,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_condition_specification import (
        EcucConditionSpecification,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_condition_formula import (
        EcucConditionFormula,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_validation_condition import (
        EcucValidationCondition,
    )

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_scope_enum import (
    EcucScopeEnum,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_configuration_class_enum import (
    EcucConfigurationClassEnum,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_configuration_variant_enum import (
    EcucConfigurationVariantEnum,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_nesting_contract_enum import (
    EcucDestinationUriNestingContractEnum,
)

__all__ = [
    "EcucAbstractConfigurationClass",
    "EcucAbstractExternalReferenceDef",
    "EcucAbstractInternalReferenceDef",
    "EcucAbstractReferenceDef",
    "EcucAbstractStringParamDef",
    "EcucAddInfoParamDef",
    "EcucBooleanParamDef",
    "EcucChoiceContainerDef",
    "EcucChoiceReferenceDef",
    "EcucCommonAttributes",
    "EcucConditionFormula",
    "EcucConditionSpecification",
    "EcucConfigurationClassEnum",
    "EcucConfigurationVariantEnum",
    "EcucContainerDef",
    "EcucDefinitionCollection",
    "EcucDefinitionElement",
    "EcucDerivationSpecification",
    "EcucDestinationUriDef",
    "EcucDestinationUriDefSet",
    "EcucDestinationUriNestingContractEnum",
    "EcucDestinationUriPolicy",
    "EcucEnumerationLiteralDef",
    "EcucEnumerationParamDef",
    "EcucFloatParamDef",
    "EcucForeignReferenceDef",
    "EcucFunctionNameDef",
    "EcucInstanceReferenceDef",
    "EcucIntegerParamDef",
    "EcucLinkerSymbolDef",
    "EcucModuleDef",
    "EcucMultilineStringParamDef",
    "EcucMultiplicityConfigurationClass",
    "EcucParamConfContainerDef",
    "EcucParameterDef",
    "EcucParameterDerivationFormula",
    "EcucQuery",
    "EcucQueryExpression",
    "EcucReferenceDef",
    "EcucScopeEnum",
    "EcucStringParamDef",
    "EcucUriReferenceDef",
    "EcucValidationCondition",
    "EcucValueConfigurationClass",
]

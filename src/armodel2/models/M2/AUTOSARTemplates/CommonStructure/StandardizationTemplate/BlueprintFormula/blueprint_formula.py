"""BlueprintFormula AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintFormula.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BlueprintFormula(ARObject):
    """AUTOSAR BlueprintFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BLUEPRINT-FORMULA"


    ecuc_ref: ARRef
    verbatim: MultiLanguageVerbatim
    _DESERIALIZE_DISPATCH = {
        "ECUC-REF": ("_POLYMORPHIC", "ecuc_ref", ["EcucAddInfoParamDef", "EcucBooleanParamDef", "EcucChoiceContainerDef", "EcucChoiceReferenceDef", "EcucCommonAttributes", "EcucContainerDef", "EcucEnumerationParamDef", "EcucFloatParamDef", "EcucForeignReferenceDef", "EcucFunctionNameDef", "EcucInstanceReferenceDef", "EcucIntegerParamDef", "EcucLinkerSymbolDef", "EcucModuleDef", "EcucMultilineStringParamDef", "EcucParamConfContainerDef", "EcucReferenceDef", "EcucStringParamDef", "EcucUriReferenceDef"]),
        "VERBATIM": lambda obj, elem: setattr(obj, "verbatim", SerializationHelper.deserialize_by_tag(elem, "MultiLanguageVerbatim")),
    }


    def __init__(self) -> None:
        """Initialize BlueprintFormula."""
        super().__init__()
        self.ecuc_ref: ARRef = None
        self.verbatim: MultiLanguageVerbatim = None

    def serialize(self) -> ET.Element:
        """Serialize BlueprintFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BlueprintFormula, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecuc_ref
        if self.ecuc_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecuc_ref, "EcucDefinitionElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize verbatim
        if self.verbatim is not None:
            serialized = SerializationHelper.serialize_item(self.verbatim, "MultiLanguageVerbatim")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERBATIM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintFormula":
        """Deserialize XML element to BlueprintFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintFormula object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BlueprintFormula, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ECUC-REF":
                setattr(obj, "ecuc_ref", ARRef.deserialize(child))
            elif tag == "VERBATIM":
                setattr(obj, "verbatim", SerializationHelper.deserialize_by_tag(child, "MultiLanguageVerbatim"))

        return obj



class BlueprintFormulaBuilder(BuilderBase):
    """Builder for BlueprintFormula with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BlueprintFormula = BlueprintFormula()


    def with_ecuc(self, value: EcucDefinitionElement) -> "BlueprintFormulaBuilder":
        """Set ecuc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecuc = value
        return self

    def with_verbatim(self, value: MultiLanguageVerbatim) -> "BlueprintFormulaBuilder":
        """Set verbatim attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.verbatim = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "ecuc",
        "verbatim",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "ecuc", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'ecuc' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'ecuc' is None", UserWarning)
        if getattr(self._obj, "verbatim", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'verbatim' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'verbatim' is None", UserWarning)


    def build(self) -> BlueprintFormula:
        """Build and return the BlueprintFormula instance with validation."""
        self._validate_instance()
        return self._obj
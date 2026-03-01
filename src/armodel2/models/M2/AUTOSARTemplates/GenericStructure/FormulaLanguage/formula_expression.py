"""FormulaExpression AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 223)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 73)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 448)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_FormulaLanguage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FormulaExpression(ARObject, ABC):
    """AUTOSAR FormulaExpression."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_reference_refs: list[ARRef]
    atp_string_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ATP-REFERENCES": ("_POLYMORPHIC_LIST", "atp_reference_refs", ["AtpDefinition", "BswDistinguishedPartition", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswVariableAccess", "CouplingPortTrafficClassAssignment", "DiagnosticEnvModeElement", "EthernetPriorityRegeneration", "ExclusiveAreaNestingOrder", "HwDescriptionEntity", "ImplementationProps", "LinSlaveConfigIdent", "ModeTransition", "MultilanguageReferrable", "PncMappingIdent", "SingleLanguageReferrable", "SoConIPduIdentifier", "SocketConnectionBundle", "TimeSyncServerConfiguration", "TpConnectionIdent"]),
        "ATP-STRINGS": ("_POLYMORPHIC_LIST", "atp_string_refs", ["AtpDefinition", "BswDistinguishedPartition", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswVariableAccess", "CouplingPortTrafficClassAssignment", "DiagnosticEnvModeElement", "EthernetPriorityRegeneration", "ExclusiveAreaNestingOrder", "HwDescriptionEntity", "ImplementationProps", "LinSlaveConfigIdent", "ModeTransition", "MultilanguageReferrable", "PncMappingIdent", "SingleLanguageReferrable", "SoConIPduIdentifier", "SocketConnectionBundle", "TimeSyncServerConfiguration", "TpConnectionIdent"]),
    }


    def __init__(self) -> None:
        """Initialize FormulaExpression."""
        super().__init__()
        self.atp_reference_refs: list[ARRef] = []
        self.atp_string_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize FormulaExpression to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FormulaExpression, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize atp_reference_refs (list to container "ATP-REFERENCE-REFS")
        if self.atp_reference_refs:
            wrapper = ET.Element("ATP-REFERENCE-REFS")
            for item in self.atp_reference_refs:
                serialized = SerializationHelper.serialize_item(item, "Referrable")
                if serialized is not None:
                    child_elem = ET.Element("ATP-REFERENCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize atp_string_refs (list to container "ATP-STRING-REFS")
        if self.atp_string_refs:
            wrapper = ET.Element("ATP-STRING-REFS")
            for item in self.atp_string_refs:
                serialized = SerializationHelper.serialize_item(item, "Referrable")
                if serialized is not None:
                    child_elem = ET.Element("ATP-STRING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FormulaExpression":
        """Deserialize XML element to FormulaExpression object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FormulaExpression object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FormulaExpression, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ATP-REFERENCES":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-DEFINITION":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AtpDefinition"))
                    elif concrete_tag == "BSW-DISTINGUISHED-PARTITION":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswDistinguishedPartition"))
                    elif concrete_tag == "BSW-MODULE-CALL-POINT":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswModuleCallPoint"))
                    elif concrete_tag == "BSW-MODULE-CLIENT-SERVER-ENTRY":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswModuleClientServerEntry"))
                    elif concrete_tag == "BSW-VARIABLE-ACCESS":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswVariableAccess"))
                    elif concrete_tag == "COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CouplingPortTrafficClassAssignment"))
                    elif concrete_tag == "DIAGNOSTIC-ENV-MODE-ELEMENT":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEnvModeElement"))
                    elif concrete_tag == "ETHERNET-PRIORITY-REGENERATION":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetPriorityRegeneration"))
                    elif concrete_tag == "EXCLUSIVE-AREA-NESTING-ORDER":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ExclusiveAreaNestingOrder"))
                    elif concrete_tag == "HW-DESCRIPTION-ENTITY":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HwDescriptionEntity"))
                    elif concrete_tag == "IMPLEMENTATION-PROPS":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ImplementationProps"))
                    elif concrete_tag == "LIN-SLAVE-CONFIG-IDENT":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinSlaveConfigIdent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ModeTransition"))
                    elif concrete_tag == "MULTILANGUAGE-REFERRABLE":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "MultilanguageReferrable"))
                    elif concrete_tag == "PNC-MAPPING-IDENT":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PncMappingIdent"))
                    elif concrete_tag == "SINGLE-LANGUAGE-REFERRABLE":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SingleLanguageReferrable"))
                    elif concrete_tag == "SO-CON-I-PDU-IDENTIFIER":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SoConIPduIdentifier"))
                    elif concrete_tag == "SOCKET-CONNECTION-BUNDLE":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SocketConnectionBundle"))
                    elif concrete_tag == "TIME-SYNC-SERVER-CONFIGURATION":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimeSyncServerConfiguration"))
                    elif concrete_tag == "TP-CONNECTION-IDENT":
                        obj.atp_reference_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TpConnectionIdent"))
            elif tag == "ATP-STRINGS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-DEFINITION":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AtpDefinition"))
                    elif concrete_tag == "BSW-DISTINGUISHED-PARTITION":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswDistinguishedPartition"))
                    elif concrete_tag == "BSW-MODULE-CALL-POINT":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswModuleCallPoint"))
                    elif concrete_tag == "BSW-MODULE-CLIENT-SERVER-ENTRY":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswModuleClientServerEntry"))
                    elif concrete_tag == "BSW-VARIABLE-ACCESS":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswVariableAccess"))
                    elif concrete_tag == "COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CouplingPortTrafficClassAssignment"))
                    elif concrete_tag == "DIAGNOSTIC-ENV-MODE-ELEMENT":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEnvModeElement"))
                    elif concrete_tag == "ETHERNET-PRIORITY-REGENERATION":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetPriorityRegeneration"))
                    elif concrete_tag == "EXCLUSIVE-AREA-NESTING-ORDER":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ExclusiveAreaNestingOrder"))
                    elif concrete_tag == "HW-DESCRIPTION-ENTITY":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HwDescriptionEntity"))
                    elif concrete_tag == "IMPLEMENTATION-PROPS":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ImplementationProps"))
                    elif concrete_tag == "LIN-SLAVE-CONFIG-IDENT":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinSlaveConfigIdent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ModeTransition"))
                    elif concrete_tag == "MULTILANGUAGE-REFERRABLE":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "MultilanguageReferrable"))
                    elif concrete_tag == "PNC-MAPPING-IDENT":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PncMappingIdent"))
                    elif concrete_tag == "SINGLE-LANGUAGE-REFERRABLE":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SingleLanguageReferrable"))
                    elif concrete_tag == "SO-CON-I-PDU-IDENTIFIER":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SoConIPduIdentifier"))
                    elif concrete_tag == "SOCKET-CONNECTION-BUNDLE":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SocketConnectionBundle"))
                    elif concrete_tag == "TIME-SYNC-SERVER-CONFIGURATION":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TimeSyncServerConfiguration"))
                    elif concrete_tag == "TP-CONNECTION-IDENT":
                        obj.atp_string_refs.append(SerializationHelper.deserialize_by_tag(child[0], "TpConnectionIdent"))

        return obj



class FormulaExpressionBuilder(BuilderBase, ABC):
    """Builder for FormulaExpression with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FormulaExpression = FormulaExpression()


    def with_atp_references(self, items: list[Referrable]) -> "FormulaExpressionBuilder":
        """Set atp_references list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.atp_references = list(items) if items else []
        return self

    def with_atp_strings(self, items: list[Referrable]) -> "FormulaExpressionBuilder":
        """Set atp_strings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.atp_strings = list(items) if items else []
        return self


    def add_atp_reference(self, item: Referrable) -> "FormulaExpressionBuilder":
        """Add a single item to atp_references list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.atp_references.append(item)
        return self

    def clear_atp_references(self) -> "FormulaExpressionBuilder":
        """Clear all items from atp_references list.

        Returns:
            self for method chaining
        """
        self._obj.atp_references = []
        return self

    def add_atp_string(self, item: Referrable) -> "FormulaExpressionBuilder":
        """Add a single item to atp_strings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.atp_strings.append(item)
        return self

    def clear_atp_strings(self) -> "FormulaExpressionBuilder":
        """Clear all items from atp_strings list.

        Returns:
            self for method chaining
        """
        self._obj.atp_strings = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    @abstractmethod
    def build(self) -> FormulaExpression:
        """Build and return the FormulaExpression instance (abstract)."""
        raise NotImplementedError
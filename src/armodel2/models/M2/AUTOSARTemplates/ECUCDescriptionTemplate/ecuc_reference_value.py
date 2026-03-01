"""EcucReferenceValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 132)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import (
    EcucAbstractReferenceValue,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import EcucAbstractReferenceValueBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucReferenceValue(EcucAbstractReferenceValue):
    """AUTOSAR EcucReferenceValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-REFERENCE-VALUE"


    value_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "VALUE-REF": ("_POLYMORPHIC", "value_ref", ["AtpDefinition", "BswDistinguishedPartition", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswVariableAccess", "CouplingPortTrafficClassAssignment", "DiagnosticEnvModeElement", "EthernetPriorityRegeneration", "ExclusiveAreaNestingOrder", "HwDescriptionEntity", "ImplementationProps", "LinSlaveConfigIdent", "ModeTransition", "MultilanguageReferrable", "PncMappingIdent", "SingleLanguageReferrable", "SoConIPduIdentifier", "SocketConnectionBundle", "TimeSyncServerConfiguration", "TpConnectionIdent"]),
    }


    def __init__(self) -> None:
        """Initialize EcucReferenceValue."""
        super().__init__()
        self.value_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucReferenceValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucReferenceValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize value_ref
        if self.value_ref is not None:
            serialized = SerializationHelper.serialize_item(self.value_ref, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucReferenceValue":
        """Deserialize XML element to EcucReferenceValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucReferenceValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucReferenceValue, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "VALUE-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-DEFINITION":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "AtpDefinition"))
                    elif concrete_tag == "BSW-DISTINGUISHED-PARTITION":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "BswDistinguishedPartition"))
                    elif concrete_tag == "BSW-MODULE-CALL-POINT":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "BswModuleCallPoint"))
                    elif concrete_tag == "BSW-MODULE-CLIENT-SERVER-ENTRY":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "BswModuleClientServerEntry"))
                    elif concrete_tag == "BSW-VARIABLE-ACCESS":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "BswVariableAccess"))
                    elif concrete_tag == "COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "CouplingPortTrafficClassAssignment"))
                    elif concrete_tag == "DIAGNOSTIC-ENV-MODE-ELEMENT":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEnvModeElement"))
                    elif concrete_tag == "ETHERNET-PRIORITY-REGENERATION":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "EthernetPriorityRegeneration"))
                    elif concrete_tag == "EXCLUSIVE-AREA-NESTING-ORDER":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "ExclusiveAreaNestingOrder"))
                    elif concrete_tag == "HW-DESCRIPTION-ENTITY":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "HwDescriptionEntity"))
                    elif concrete_tag == "IMPLEMENTATION-PROPS":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "ImplementationProps"))
                    elif concrete_tag == "LIN-SLAVE-CONFIG-IDENT":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "LinSlaveConfigIdent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "ModeTransition"))
                    elif concrete_tag == "MULTILANGUAGE-REFERRABLE":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "MultilanguageReferrable"))
                    elif concrete_tag == "PNC-MAPPING-IDENT":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "PncMappingIdent"))
                    elif concrete_tag == "SINGLE-LANGUAGE-REFERRABLE":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "SingleLanguageReferrable"))
                    elif concrete_tag == "SO-CON-I-PDU-IDENTIFIER":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "SoConIPduIdentifier"))
                    elif concrete_tag == "SOCKET-CONNECTION-BUNDLE":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "SocketConnectionBundle"))
                    elif concrete_tag == "TIME-SYNC-SERVER-CONFIGURATION":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "TimeSyncServerConfiguration"))
                    elif concrete_tag == "TP-CONNECTION-IDENT":
                        setattr(obj, "value_ref", SerializationHelper.deserialize_by_tag(child[0], "TpConnectionIdent"))

        return obj



class EcucReferenceValueBuilder(EcucAbstractReferenceValueBuilder):
    """Builder for EcucReferenceValue with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucReferenceValue = EcucReferenceValue()


    def with_value(self, value: Optional[Referrable]) -> "EcucReferenceValueBuilder":
        """Set value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value = value
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


    def build(self) -> EcucReferenceValue:
        """Build and return the EcucReferenceValue instance with validation."""
        self._validate_instance()
        pass
        return self._obj
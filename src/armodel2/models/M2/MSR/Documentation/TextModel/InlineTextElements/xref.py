"""Xref AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 320)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    ResolutionPolicyEnum,
    ShowContentEnum,
    ShowResourceAliasNameEnum,
    ShowResourceLongNameEnum,
    ShowResourceNumberEnum,
    ShowResourcePageEnum,
    ShowResourceShortNameEnum,
    ShowResourceTypeEnum,
    ShowSeeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_long_name import (
    SingleLanguageLongName,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Xref(ARObject):
    """AUTOSAR Xref."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "XREF"


    label1: Optional[SingleLanguageLongName]
    referrable_ref: Optional[ARRef]
    resolution_policy_enum: Optional[ResolutionPolicyEnum]
    show_content_enum: Optional[ShowContentEnum]
    show_resource_alias: Optional[ShowResourceAliasNameEnum]
    show_resource: Optional[ShowResourceTypeEnum]
    show_resource_long: Optional[ShowResourceLongNameEnum]
    show_resource_number: Optional[ShowResourceNumberEnum]
    show_resource_page: Optional[ShowResourcePageEnum]
    show_resource_short: Optional[ShowResourceShortNameEnum]
    show_see: Optional[ShowSeeEnum]
    _DESERIALIZE_DISPATCH = {
        "LABEL1": lambda obj, elem: setattr(obj, "label1", SerializationHelper.deserialize_by_tag(elem, "SingleLanguageLongName")),
        "REFERRABLE-REF": ("_POLYMORPHIC", "referrable_ref", ["AtpDefinition", "BswDistinguishedPartition", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswVariableAccess", "CouplingPortTrafficClassAssignment", "DiagnosticEnvModeElement", "EthernetPriorityRegeneration", "ExclusiveAreaNestingOrder", "HwDescriptionEntity", "ImplementationProps", "LinSlaveConfigIdent", "ModeTransition", "MultilanguageReferrable", "PncMappingIdent", "SingleLanguageReferrable", "SoConIPduIdentifier", "SocketConnectionBundle", "TimeSyncServerConfiguration", "TpConnectionIdent"]),
        "RESOLUTION-POLICY-ENUM": lambda obj, elem: setattr(obj, "resolution_policy_enum", ResolutionPolicyEnum.deserialize(elem)),
        "SHOW-CONTENT-ENUM": lambda obj, elem: setattr(obj, "show_content_enum", ShowContentEnum.deserialize(elem)),
        "SHOW-RESOURCE-ALIAS": lambda obj, elem: setattr(obj, "show_resource_alias", ShowResourceAliasNameEnum.deserialize(elem)),
        "SHOW-RESOURCE": lambda obj, elem: setattr(obj, "show_resource", ShowResourceTypeEnum.deserialize(elem)),
        "SHOW-RESOURCE-LONG": lambda obj, elem: setattr(obj, "show_resource_long", ShowResourceLongNameEnum.deserialize(elem)),
        "SHOW-RESOURCE-NUMBER": lambda obj, elem: setattr(obj, "show_resource_number", ShowResourceNumberEnum.deserialize(elem)),
        "SHOW-RESOURCE-PAGE": lambda obj, elem: setattr(obj, "show_resource_page", ShowResourcePageEnum.deserialize(elem)),
        "SHOW-RESOURCE-SHORT": lambda obj, elem: setattr(obj, "show_resource_short", ShowResourceShortNameEnum.deserialize(elem)),
        "SHOW-SEE": lambda obj, elem: setattr(obj, "show_see", ShowSeeEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize Xref."""
        super().__init__()
        self.label1: Optional[SingleLanguageLongName] = None
        self.referrable_ref: Optional[ARRef] = None
        self.resolution_policy_enum: Optional[ResolutionPolicyEnum] = None
        self.show_content_enum: Optional[ShowContentEnum] = None
        self.show_resource_alias: Optional[ShowResourceAliasNameEnum] = None
        self.show_resource: Optional[ShowResourceTypeEnum] = None
        self.show_resource_long: Optional[ShowResourceLongNameEnum] = None
        self.show_resource_number: Optional[ShowResourceNumberEnum] = None
        self.show_resource_page: Optional[ShowResourcePageEnum] = None
        self.show_resource_short: Optional[ShowResourceShortNameEnum] = None
        self.show_see: Optional[ShowSeeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize Xref to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Xref, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize label1
        if self.label1 is not None:
            serialized = SerializationHelper.serialize_item(self.label1, "SingleLanguageLongName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LABEL1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize referrable_ref
        if self.referrable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.referrable_ref, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERRABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize resolution_policy_enum
        if self.resolution_policy_enum is not None:
            serialized = SerializationHelper.serialize_item(self.resolution_policy_enum, "ResolutionPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOLUTION-POLICY-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_content_enum
        if self.show_content_enum is not None:
            serialized = SerializationHelper.serialize_item(self.show_content_enum, "ShowContentEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-CONTENT-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_alias
        if self.show_resource_alias is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_alias, "ShowResourceAliasNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-ALIAS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource
        if self.show_resource is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource, "ShowResourceTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_long
        if self.show_resource_long is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_long, "ShowResourceLongNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-LONG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_number
        if self.show_resource_number is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_number, "ShowResourceNumberEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_page
        if self.show_resource_page is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_page, "ShowResourcePageEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-PAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_resource_short
        if self.show_resource_short is not None:
            serialized = SerializationHelper.serialize_item(self.show_resource_short, "ShowResourceShortNameEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-RESOURCE-SHORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize show_see
        if self.show_see is not None:
            serialized = SerializationHelper.serialize_item(self.show_see, "ShowSeeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHOW-SEE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xref":
        """Deserialize XML element to Xref object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Xref object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Xref, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "LABEL1":
                setattr(obj, "label1", SerializationHelper.deserialize_by_tag(child, "SingleLanguageLongName"))
            elif tag == "REFERRABLE-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-DEFINITION":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "AtpDefinition"))
                    elif concrete_tag == "BSW-DISTINGUISHED-PARTITION":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "BswDistinguishedPartition"))
                    elif concrete_tag == "BSW-MODULE-CALL-POINT":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "BswModuleCallPoint"))
                    elif concrete_tag == "BSW-MODULE-CLIENT-SERVER-ENTRY":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "BswModuleClientServerEntry"))
                    elif concrete_tag == "BSW-VARIABLE-ACCESS":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "BswVariableAccess"))
                    elif concrete_tag == "COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "CouplingPortTrafficClassAssignment"))
                    elif concrete_tag == "DIAGNOSTIC-ENV-MODE-ELEMENT":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEnvModeElement"))
                    elif concrete_tag == "ETHERNET-PRIORITY-REGENERATION":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "EthernetPriorityRegeneration"))
                    elif concrete_tag == "EXCLUSIVE-AREA-NESTING-ORDER":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "ExclusiveAreaNestingOrder"))
                    elif concrete_tag == "HW-DESCRIPTION-ENTITY":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "HwDescriptionEntity"))
                    elif concrete_tag == "IMPLEMENTATION-PROPS":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "ImplementationProps"))
                    elif concrete_tag == "LIN-SLAVE-CONFIG-IDENT":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "LinSlaveConfigIdent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "ModeTransition"))
                    elif concrete_tag == "MULTILANGUAGE-REFERRABLE":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "MultilanguageReferrable"))
                    elif concrete_tag == "PNC-MAPPING-IDENT":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "PncMappingIdent"))
                    elif concrete_tag == "SINGLE-LANGUAGE-REFERRABLE":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "SingleLanguageReferrable"))
                    elif concrete_tag == "SO-CON-I-PDU-IDENTIFIER":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "SoConIPduIdentifier"))
                    elif concrete_tag == "SOCKET-CONNECTION-BUNDLE":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "SocketConnectionBundle"))
                    elif concrete_tag == "TIME-SYNC-SERVER-CONFIGURATION":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "TimeSyncServerConfiguration"))
                    elif concrete_tag == "TP-CONNECTION-IDENT":
                        setattr(obj, "referrable_ref", SerializationHelper.deserialize_by_tag(child[0], "TpConnectionIdent"))
            elif tag == "RESOLUTION-POLICY-ENUM":
                setattr(obj, "resolution_policy_enum", ResolutionPolicyEnum.deserialize(child))
            elif tag == "SHOW-CONTENT-ENUM":
                setattr(obj, "show_content_enum", ShowContentEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE-ALIAS":
                setattr(obj, "show_resource_alias", ShowResourceAliasNameEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE":
                setattr(obj, "show_resource", ShowResourceTypeEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE-LONG":
                setattr(obj, "show_resource_long", ShowResourceLongNameEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE-NUMBER":
                setattr(obj, "show_resource_number", ShowResourceNumberEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE-PAGE":
                setattr(obj, "show_resource_page", ShowResourcePageEnum.deserialize(child))
            elif tag == "SHOW-RESOURCE-SHORT":
                setattr(obj, "show_resource_short", ShowResourceShortNameEnum.deserialize(child))
            elif tag == "SHOW-SEE":
                setattr(obj, "show_see", ShowSeeEnum.deserialize(child))

        return obj



class XrefBuilder(BuilderBase):
    """Builder for Xref with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Xref = Xref()


    def with_label1(self, value: Optional[SingleLanguageLongName]) -> "XrefBuilder":
        """Set label1 attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.label1 = value
        return self

    def with_referrable(self, value: Optional[Referrable]) -> "XrefBuilder":
        """Set referrable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.referrable = value
        return self

    def with_resolution_policy_enum(self, value: Optional[ResolutionPolicyEnum]) -> "XrefBuilder":
        """Set resolution_policy_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resolution_policy_enum = value
        return self

    def with_show_content_enum(self, value: Optional[ShowContentEnum]) -> "XrefBuilder":
        """Set show_content_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_content_enum = value
        return self

    def with_show_resource_alias(self, value: Optional[ShowResourceAliasNameEnum]) -> "XrefBuilder":
        """Set show_resource_alias attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_alias = value
        return self

    def with_show_resource(self, value: Optional[ShowResourceTypeEnum]) -> "XrefBuilder":
        """Set show_resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource = value
        return self

    def with_show_resource_long(self, value: Optional[ShowResourceLongNameEnum]) -> "XrefBuilder":
        """Set show_resource_long attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_long = value
        return self

    def with_show_resource_number(self, value: Optional[ShowResourceNumberEnum]) -> "XrefBuilder":
        """Set show_resource_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_number = value
        return self

    def with_show_resource_page(self, value: Optional[ShowResourcePageEnum]) -> "XrefBuilder":
        """Set show_resource_page attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_page = value
        return self

    def with_show_resource_short(self, value: Optional[ShowResourceShortNameEnum]) -> "XrefBuilder":
        """Set show_resource_short attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_resource_short = value
        return self

    def with_show_see(self, value: Optional[ShowSeeEnum]) -> "XrefBuilder":
        """Set show_see attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.show_see = value
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


    def build(self) -> Xref:
        """Build and return the Xref instance with validation."""
        self._validate_instance()
        pass
        return self._obj
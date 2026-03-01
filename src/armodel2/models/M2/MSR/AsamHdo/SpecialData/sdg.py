"""Sdg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1004)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 78)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sd import (
    Sd,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdf import (
    Sdf,
)
from armodel2.models.M2.MSR.AsamHdo.SpecialData.sdg_caption import (
    SdgCaption,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Sdg(ARObject):
    """AUTOSAR Sdg."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SDG"


    gid: NameToken
    sdg_caption: Optional[SdgCaption]
    sd: Optional[Sd]
    sdf: Optional[Sdf]
    sdg: Optional[Sdg]
    sdx: Optional[Referrable]
    sdxf: Optional[Referrable]
    _DESERIALIZE_DISPATCH = {
        "GID": lambda obj, elem: setattr(obj, "gid", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "SDG-CAPTION": lambda obj, elem: setattr(obj, "sdg_caption", SerializationHelper.deserialize_by_tag(elem, "SdgCaption")),
        "SD": lambda obj, elem: setattr(obj, "sd", SerializationHelper.deserialize_by_tag(elem, "Sd")),
        "SDF": lambda obj, elem: setattr(obj, "sdf", SerializationHelper.deserialize_by_tag(elem, "Sdf")),
        "SDG": lambda obj, elem: setattr(obj, "sdg", SerializationHelper.deserialize_by_tag(elem, "Sdg")),
        "SDX": ("_POLYMORPHIC", "sdx", ["AtpDefinition", "BswDistinguishedPartition", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswVariableAccess", "CouplingPortTrafficClassAssignment", "DiagnosticEnvModeElement", "EthernetPriorityRegeneration", "ExclusiveAreaNestingOrder", "HwDescriptionEntity", "ImplementationProps", "LinSlaveConfigIdent", "ModeTransition", "MultilanguageReferrable", "PncMappingIdent", "SingleLanguageReferrable", "SoConIPduIdentifier", "SocketConnectionBundle", "TimeSyncServerConfiguration", "TpConnectionIdent"]),
        "SDXF": ("_POLYMORPHIC", "sdxf", ["AtpDefinition", "BswDistinguishedPartition", "BswModuleCallPoint", "BswModuleClientServerEntry", "BswVariableAccess", "CouplingPortTrafficClassAssignment", "DiagnosticEnvModeElement", "EthernetPriorityRegeneration", "ExclusiveAreaNestingOrder", "HwDescriptionEntity", "ImplementationProps", "LinSlaveConfigIdent", "ModeTransition", "MultilanguageReferrable", "PncMappingIdent", "SingleLanguageReferrable", "SoConIPduIdentifier", "SocketConnectionBundle", "TimeSyncServerConfiguration", "TpConnectionIdent"]),
    }


    def __init__(self) -> None:
        """Initialize Sdg."""
        super().__init__()
        self.gid: NameToken = None
        self.sdg_caption: Optional[SdgCaption] = None
        self.sd: Optional[Sd] = None
        self.sdf: Optional[Sdf] = None
        self.sdg: Optional[Sdg] = None
        self.sdx: Optional[Referrable] = None
        self.sdxf: Optional[Referrable] = None

    def serialize(self) -> ET.Element:
        """Serialize Sdg to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Sdg, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize gid
        if self.gid is not None:
            serialized = SerializationHelper.serialize_item(self.gid, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdg_caption
        if self.sdg_caption is not None:
            serialized = SerializationHelper.serialize_item(self.sdg_caption, "SdgCaption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDG-CAPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sd
        if self.sd is not None:
            serialized = SerializationHelper.serialize_item(self.sd, "Sd")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdf
        if self.sdf is not None:
            serialized = SerializationHelper.serialize_item(self.sdf, "Sdf")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdg
        if self.sdg is not None:
            serialized = SerializationHelper.serialize_item(self.sdg, "Sdg")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdx
        if self.sdx is not None:
            serialized = SerializationHelper.serialize_item(self.sdx, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdxf
        if self.sdxf is not None:
            serialized = SerializationHelper.serialize_item(self.sdxf, "Referrable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SDXF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sdg":
        """Deserialize XML element to Sdg object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Sdg object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Sdg, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "GID":
                setattr(obj, "gid", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "SDG-CAPTION":
                setattr(obj, "sdg_caption", SerializationHelper.deserialize_by_tag(child, "SdgCaption"))
            elif tag == "SD":
                setattr(obj, "sd", SerializationHelper.deserialize_by_tag(child, "Sd"))
            elif tag == "SDF":
                setattr(obj, "sdf", SerializationHelper.deserialize_by_tag(child, "Sdf"))
            elif tag == "SDG":
                setattr(obj, "sdg", SerializationHelper.deserialize_by_tag(child, "Sdg"))
            elif tag == "SDX":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-DEFINITION":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "AtpDefinition"))
                    elif concrete_tag == "BSW-DISTINGUISHED-PARTITION":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "BswDistinguishedPartition"))
                    elif concrete_tag == "BSW-MODULE-CALL-POINT":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "BswModuleCallPoint"))
                    elif concrete_tag == "BSW-MODULE-CLIENT-SERVER-ENTRY":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "BswModuleClientServerEntry"))
                    elif concrete_tag == "BSW-VARIABLE-ACCESS":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "BswVariableAccess"))
                    elif concrete_tag == "COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "CouplingPortTrafficClassAssignment"))
                    elif concrete_tag == "DIAGNOSTIC-ENV-MODE-ELEMENT":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEnvModeElement"))
                    elif concrete_tag == "ETHERNET-PRIORITY-REGENERATION":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "EthernetPriorityRegeneration"))
                    elif concrete_tag == "EXCLUSIVE-AREA-NESTING-ORDER":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "ExclusiveAreaNestingOrder"))
                    elif concrete_tag == "HW-DESCRIPTION-ENTITY":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "HwDescriptionEntity"))
                    elif concrete_tag == "IMPLEMENTATION-PROPS":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "ImplementationProps"))
                    elif concrete_tag == "LIN-SLAVE-CONFIG-IDENT":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "LinSlaveConfigIdent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "ModeTransition"))
                    elif concrete_tag == "MULTILANGUAGE-REFERRABLE":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "MultilanguageReferrable"))
                    elif concrete_tag == "PNC-MAPPING-IDENT":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "PncMappingIdent"))
                    elif concrete_tag == "SINGLE-LANGUAGE-REFERRABLE":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "SingleLanguageReferrable"))
                    elif concrete_tag == "SO-CON-I-PDU-IDENTIFIER":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "SoConIPduIdentifier"))
                    elif concrete_tag == "SOCKET-CONNECTION-BUNDLE":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "SocketConnectionBundle"))
                    elif concrete_tag == "TIME-SYNC-SERVER-CONFIGURATION":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "TimeSyncServerConfiguration"))
                    elif concrete_tag == "TP-CONNECTION-IDENT":
                        setattr(obj, "sdx", SerializationHelper.deserialize_by_tag(child[0], "TpConnectionIdent"))
            elif tag == "SDXF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-DEFINITION":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "AtpDefinition"))
                    elif concrete_tag == "BSW-DISTINGUISHED-PARTITION":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "BswDistinguishedPartition"))
                    elif concrete_tag == "BSW-MODULE-CALL-POINT":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "BswModuleCallPoint"))
                    elif concrete_tag == "BSW-MODULE-CLIENT-SERVER-ENTRY":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "BswModuleClientServerEntry"))
                    elif concrete_tag == "BSW-VARIABLE-ACCESS":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "BswVariableAccess"))
                    elif concrete_tag == "COUPLING-PORT-TRAFFIC-CLASS-ASSIGNMENT":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "CouplingPortTrafficClassAssignment"))
                    elif concrete_tag == "DIAGNOSTIC-ENV-MODE-ELEMENT":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEnvModeElement"))
                    elif concrete_tag == "ETHERNET-PRIORITY-REGENERATION":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "EthernetPriorityRegeneration"))
                    elif concrete_tag == "EXCLUSIVE-AREA-NESTING-ORDER":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "ExclusiveAreaNestingOrder"))
                    elif concrete_tag == "HW-DESCRIPTION-ENTITY":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "HwDescriptionEntity"))
                    elif concrete_tag == "IMPLEMENTATION-PROPS":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "ImplementationProps"))
                    elif concrete_tag == "LIN-SLAVE-CONFIG-IDENT":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "LinSlaveConfigIdent"))
                    elif concrete_tag == "MODE-TRANSITION":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "ModeTransition"))
                    elif concrete_tag == "MULTILANGUAGE-REFERRABLE":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "MultilanguageReferrable"))
                    elif concrete_tag == "PNC-MAPPING-IDENT":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "PncMappingIdent"))
                    elif concrete_tag == "SINGLE-LANGUAGE-REFERRABLE":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "SingleLanguageReferrable"))
                    elif concrete_tag == "SO-CON-I-PDU-IDENTIFIER":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "SoConIPduIdentifier"))
                    elif concrete_tag == "SOCKET-CONNECTION-BUNDLE":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "SocketConnectionBundle"))
                    elif concrete_tag == "TIME-SYNC-SERVER-CONFIGURATION":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "TimeSyncServerConfiguration"))
                    elif concrete_tag == "TP-CONNECTION-IDENT":
                        setattr(obj, "sdxf", SerializationHelper.deserialize_by_tag(child[0], "TpConnectionIdent"))

        return obj



class SdgBuilder(BuilderBase):
    """Builder for Sdg with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Sdg = Sdg()


    def with_gid(self, value: NameToken) -> "SdgBuilder":
        """Set gid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.gid = value
        return self

    def with_sdg_caption(self, value: Optional[SdgCaption]) -> "SdgBuilder":
        """Set sdg_caption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdg_caption = value
        return self

    def with_sd(self, value: Optional[Sd]) -> "SdgBuilder":
        """Set sd attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd = value
        return self

    def with_sdf(self, value: Optional[Sdf]) -> "SdgBuilder":
        """Set sdf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdf = value
        return self

    def with_sdg(self, value: Optional[Sdg]) -> "SdgBuilder":
        """Set sdg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdg = value
        return self

    def with_sdx(self, value: Optional[Referrable]) -> "SdgBuilder":
        """Set sdx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdx = value
        return self

    def with_sdxf(self, value: Optional[Referrable]) -> "SdgBuilder":
        """Set sdxf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sdxf = value
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


    def build(self) -> Sdg:
        """Build and return the Sdg instance with validation."""
        self._validate_instance()
        pass
        return self._obj
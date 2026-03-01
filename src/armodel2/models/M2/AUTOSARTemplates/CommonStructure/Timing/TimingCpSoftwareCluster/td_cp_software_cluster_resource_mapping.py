"""TDCpSoftwareClusterResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDCpSoftwareClusterResourceMapping(Identifiable):
    """AUTOSAR TDCpSoftwareClusterResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-CP-SOFTWARE-CLUSTER-RESOURCE-MAPPING"


    resource_ref: Optional[ARRef]
    timing_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "RESOURCE-REF": lambda obj, elem: setattr(obj, "resource_ref", ARRef.deserialize(elem)),
        "TIMING-REF": ("_POLYMORPHIC", "timing_ref", ["TimingDescriptionEvent", "TimingDescriptionEventChain"]),
    }


    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterResourceMapping."""
        super().__init__()
        self.resource_ref: Optional[ARRef] = None
        self.timing_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TDCpSoftwareClusterResourceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDCpSoftwareClusterResourceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize resource_ref
        if self.resource_ref is not None:
            serialized = SerializationHelper.serialize_item(self.resource_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOURCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_ref
        if self.timing_ref is not None:
            serialized = SerializationHelper.serialize_item(self.timing_ref, "TimingDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDCpSoftwareClusterResourceMapping":
        """Deserialize XML element to TDCpSoftwareClusterResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDCpSoftwareClusterResourceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDCpSoftwareClusterResourceMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RESOURCE-REF":
                setattr(obj, "resource_ref", ARRef.deserialize(child))
            elif tag == "TIMING-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "TIMING-DESCRIPTION-EVENT":
                        setattr(obj, "timing_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingDescriptionEvent"))
                    elif concrete_tag == "TIMING-DESCRIPTION-EVENT-CHAIN":
                        setattr(obj, "timing_ref", SerializationHelper.deserialize_by_tag(child[0], "TimingDescriptionEventChain"))

        return obj



class TDCpSoftwareClusterResourceMappingBuilder(IdentifiableBuilder):
    """Builder for TDCpSoftwareClusterResourceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDCpSoftwareClusterResourceMapping = TDCpSoftwareClusterResourceMapping()


    def with_resource(self, value: Optional[CpSoftwareCluster]) -> "TDCpSoftwareClusterResourceMappingBuilder":
        """Set resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resource = value
        return self

    def with_timing(self, value: Optional[TimingDescription]) -> "TDCpSoftwareClusterResourceMappingBuilder":
        """Set timing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timing = value
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


    def build(self) -> TDCpSoftwareClusterResourceMapping:
        """Build and return the TDCpSoftwareClusterResourceMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj
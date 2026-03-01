"""TDCpSoftwareClusterMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 156)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDCpSoftwareClusterMappingSet(ARElement):
    """AUTOSAR TDCpSoftwareClusterMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-CP-SOFTWARE-CLUSTER-MAPPING-SET"


    td_cp_softwares: list[Any]
    _DESERIALIZE_DISPATCH = {
        "TD-CP-SOFTWARES": lambda obj, elem: obj.td_cp_softwares.append(SerializationHelper.deserialize_by_tag(elem, "any (TDCpSoftwareCluster)")),
    }


    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterMappingSet."""
        super().__init__()
        self.td_cp_softwares: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize TDCpSoftwareClusterMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDCpSoftwareClusterMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize td_cp_softwares (list to container "TD-CP-SOFTWARES")
        if self.td_cp_softwares:
            wrapper = ET.Element("TD-CP-SOFTWARES")
            for item in self.td_cp_softwares:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDCpSoftwareClusterMappingSet":
        """Deserialize XML element to TDCpSoftwareClusterMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDCpSoftwareClusterMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDCpSoftwareClusterMappingSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TD-CP-SOFTWARES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.td_cp_softwares.append(SerializationHelper.deserialize_by_tag(item_elem, "any (TDCpSoftwareCluster)"))

        return obj



class TDCpSoftwareClusterMappingSetBuilder(ARElementBuilder):
    """Builder for TDCpSoftwareClusterMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDCpSoftwareClusterMappingSet = TDCpSoftwareClusterMappingSet()


    def with_td_cp_softwares(self, items: list[any (TDCpSoftwareCluster)]) -> "TDCpSoftwareClusterMappingSetBuilder":
        """Set td_cp_softwares list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.td_cp_softwares = list(items) if items else []
        return self


    def add_td_cp_software(self, item: any (TDCpSoftwareCluster)) -> "TDCpSoftwareClusterMappingSetBuilder":
        """Add a single item to td_cp_softwares list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.td_cp_softwares.append(item)
        return self

    def clear_td_cp_softwares(self) -> "TDCpSoftwareClusterMappingSetBuilder":
        """Clear all items from td_cp_softwares list.

        Returns:
            self for method chaining
        """
        self._obj.td_cp_softwares = []
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


    def build(self) -> TDCpSoftwareClusterMappingSet:
        """Build and return the TDCpSoftwareClusterMappingSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj
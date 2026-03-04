"""J1939SharedAddressCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 694)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.j1939_cluster import (
    J1939Cluster,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class J1939SharedAddressCluster(Identifiable):
    """AUTOSAR J1939SharedAddressCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "J1939-SHARED-ADDRESS-CLUSTER"


    participating_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PARTICIPATING-REFS": lambda obj, elem: [obj.participating_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize J1939SharedAddressCluster."""
        super().__init__()
        self.participating_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize J1939SharedAddressCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939SharedAddressCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize participating_refs (list to container "PARTICIPATING-REFS")
        if self.participating_refs:
            wrapper = ET.Element("PARTICIPATING-REFS")
            for item in self.participating_refs:
                serialized = SerializationHelper.serialize_item(item, "J1939Cluster")
                if serialized is not None:
                    child_elem = ET.Element("PARTICIPATING-REF")
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
    def deserialize(cls, element: ET.Element) -> "J1939SharedAddressCluster":
        """Deserialize XML element to J1939SharedAddressCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939SharedAddressCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939SharedAddressCluster, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PARTICIPATING-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.participating_refs.append(ARRef.deserialize(item_elem))

        return obj



class J1939SharedAddressClusterBuilder(IdentifiableBuilder):
    """Builder for J1939SharedAddressCluster with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: J1939SharedAddressCluster = J1939SharedAddressCluster()


    def with_participatings(self, items: list[J1939Cluster]) -> "J1939SharedAddressClusterBuilder":
        """Set participatings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.participatings = list(items) if items else []
        return self


    def add_participating(self, item: J1939Cluster) -> "J1939SharedAddressClusterBuilder":
        """Add a single item to participatings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.participatings.append(item)
        return self

    def clear_participatings(self) -> "J1939SharedAddressClusterBuilder":
        """Clear all items from participatings list.

        Returns:
            self for method chaining
        """
        self._obj.participatings = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "participating",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> J1939SharedAddressCluster:
        """Build and return the J1939SharedAddressCluster instance with validation."""
        self._validate_instance()
        return self._obj
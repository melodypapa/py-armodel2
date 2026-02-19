"""NmCoordinator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
        NmNode,
    )



class NmCoordinator(ARObject):
    """AUTOSAR NmCoordinator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    index: Optional[Integer]
    nm_coord_sync: Optional[Boolean]
    nm_global: Optional[TimeValue]
    nm_nodes: list[NmNode]
    def __init__(self) -> None:
        """Initialize NmCoordinator."""
        super().__init__()
        self.index: Optional[Integer] = None
        self.nm_coord_sync: Optional[Boolean] = None
        self.nm_global: Optional[TimeValue] = None
        self.nm_nodes: list[NmNode] = []

    def serialize(self) -> ET.Element:
        """Serialize NmCoordinator to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize index
        if self.index is not None:
            serialized = ARObject._serialize_item(self.index, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_coord_sync
        if self.nm_coord_sync is not None:
            serialized = ARObject._serialize_item(self.nm_coord_sync, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-COORD-SYNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_global
        if self.nm_global is not None:
            serialized = ARObject._serialize_item(self.nm_global, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-GLOBAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_nodes (list to container "NM-NODES")
        if self.nm_nodes:
            wrapper = ET.Element("NM-NODES")
            for item in self.nm_nodes:
                serialized = ARObject._serialize_item(item, "NmNode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmCoordinator":
        """Deserialize XML element to NmCoordinator object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmCoordinator object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse index
        child = ARObject._find_child_element(element, "INDEX")
        if child is not None:
            index_value = child.text
            obj.index = index_value

        # Parse nm_coord_sync
        child = ARObject._find_child_element(element, "NM-COORD-SYNC")
        if child is not None:
            nm_coord_sync_value = child.text
            obj.nm_coord_sync = nm_coord_sync_value

        # Parse nm_global
        child = ARObject._find_child_element(element, "NM-GLOBAL")
        if child is not None:
            nm_global_value = child.text
            obj.nm_global = nm_global_value

        # Parse nm_nodes (list from container "NM-NODES")
        obj.nm_nodes = []
        container = ARObject._find_child_element(element, "NM-NODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nm_nodes.append(child_value)

        return obj



class NmCoordinatorBuilder:
    """Builder for NmCoordinator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NmCoordinator = NmCoordinator()

    def build(self) -> NmCoordinator:
        """Build and return NmCoordinator object.

        Returns:
            NmCoordinator instance
        """
        # TODO: Add validation
        return self._obj

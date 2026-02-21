"""CpSoftwareClusterResourcePool AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 901)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class CpSoftwareClusterResourcePool(ARElement):
    """AUTOSAR CpSoftwareClusterResourcePool."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu_scope_refs: list[ARRef]
    resources: list[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResourcePool."""
        super().__init__()
        self.ecu_scope_refs: list[ARRef] = []
        self.resources: list[CpSoftwareCluster] = []

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterResourcePool to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterResourcePool, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecu_scope_refs (list to container "ECU-SCOPE-REFS")
        if self.ecu_scope_refs:
            wrapper = ET.Element("ECU-SCOPE-REFS")
            for item in self.ecu_scope_refs:
                serialized = SerializationHelper.serialize_item(item, "EcuInstance")
                if serialized is not None:
                    child_elem = ET.Element("ECU-SCOPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resources (list to container "RESOURCES")
        if self.resources:
            wrapper = ET.Element("RESOURCES")
            for item in self.resources:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterResourcePool":
        """Deserialize XML element to CpSoftwareClusterResourcePool object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterResourcePool object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterResourcePool, cls).deserialize(element)

        # Parse ecu_scope_refs (list from container "ECU-SCOPE-REFS")
        obj.ecu_scope_refs = []
        container = SerializationHelper.find_child_element(element, "ECU-SCOPE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecu_scope_refs.append(child_value)

        # Parse resources (list from container "RESOURCES")
        obj.resources = []
        container = SerializationHelper.find_child_element(element, "RESOURCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resources.append(child_value)

        return obj



class CpSoftwareClusterResourcePoolBuilder:
    """Builder for CpSoftwareClusterResourcePool."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterResourcePool = CpSoftwareClusterResourcePool()

    def build(self) -> CpSoftwareClusterResourcePool:
        """Build and return CpSoftwareClusterResourcePool object.

        Returns:
            CpSoftwareClusterResourcePool instance
        """
        # TODO: Add validation
        return self._obj

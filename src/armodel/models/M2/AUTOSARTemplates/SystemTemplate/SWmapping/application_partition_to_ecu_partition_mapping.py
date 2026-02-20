"""ApplicationPartitionToEcuPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.ecu_partition import (
    EcuPartition,
)


class ApplicationPartitionToEcuPartitionMapping(Identifiable):
    """AUTOSAR ApplicationPartitionToEcuPartitionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applications: list[ApplicationPartition]
    ecu_partition: Optional[EcuPartition]
    def __init__(self) -> None:
        """Initialize ApplicationPartitionToEcuPartitionMapping."""
        super().__init__()
        self.applications: list[ApplicationPartition] = []
        self.ecu_partition: Optional[EcuPartition] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationPartitionToEcuPartitionMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationPartitionToEcuPartitionMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize applications (list to container "APPLICATIONS")
        if self.applications:
            wrapper = ET.Element("APPLICATIONS")
            for item in self.applications:
                serialized = ARObject._serialize_item(item, "ApplicationPartition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_partition
        if self.ecu_partition is not None:
            serialized = ARObject._serialize_item(self.ecu_partition, "EcuPartition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-PARTITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationPartitionToEcuPartitionMapping":
        """Deserialize XML element to ApplicationPartitionToEcuPartitionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationPartitionToEcuPartitionMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationPartitionToEcuPartitionMapping, cls).deserialize(element)

        # Parse applications (list from container "APPLICATIONS")
        obj.applications = []
        container = ARObject._find_child_element(element, "APPLICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.applications.append(child_value)

        # Parse ecu_partition
        child = ARObject._find_child_element(element, "ECU-PARTITION")
        if child is not None:
            ecu_partition_value = ARObject._deserialize_by_tag(child, "EcuPartition")
            obj.ecu_partition = ecu_partition_value

        return obj



class ApplicationPartitionToEcuPartitionMappingBuilder:
    """Builder for ApplicationPartitionToEcuPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationPartitionToEcuPartitionMapping = ApplicationPartitionToEcuPartitionMapping()

    def build(self) -> ApplicationPartitionToEcuPartitionMapping:
        """Build and return ApplicationPartitionToEcuPartitionMapping object.

        Returns:
            ApplicationPartitionToEcuPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj

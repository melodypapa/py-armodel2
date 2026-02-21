"""BswServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 978)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
    ServiceDependency,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.role_based_bsw_module_entry_assignment import (
    RoleBasedBswModuleEntryAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class BswServiceDependency(ServiceDependency):
    """AUTOSAR BswServiceDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_datas: list[Any]
    assigned_entries: list[RoleBasedBswModuleEntryAssignment]
    ident: Optional[Any]
    service_needs: Optional[ServiceNeeds]
    def __init__(self) -> None:
        """Initialize BswServiceDependency."""
        super().__init__()
        self.assigned_datas: list[Any] = []
        self.assigned_entries: list[RoleBasedBswModuleEntryAssignment] = []
        self.ident: Optional[Any] = None
        self.service_needs: Optional[ServiceNeeds] = None

    def serialize(self) -> ET.Element:
        """Serialize BswServiceDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswServiceDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assigned_datas (list to container "ASSIGNED-DATAS")
        if self.assigned_datas:
            wrapper = ET.Element("ASSIGNED-DATAS")
            for item in self.assigned_datas:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize assigned_entries (list to container "ASSIGNED-ENTRIES")
        if self.assigned_entries:
            wrapper = ET.Element("ASSIGNED-ENTRIES")
            for item in self.assigned_entries:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedBswModuleEntryAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ident
        if self.ident is not None:
            serialized = SerializationHelper.serialize_item(self.ident, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_needs
        if self.service_needs is not None:
            serialized = SerializationHelper.serialize_item(self.service_needs, "ServiceNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-NEEDS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswServiceDependency":
        """Deserialize XML element to BswServiceDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswServiceDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswServiceDependency, cls).deserialize(element)

        # Parse assigned_datas (list from container "ASSIGNED-DATAS")
        obj.assigned_datas = []
        container = SerializationHelper.find_child_element(element, "ASSIGNED-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_datas.append(child_value)

        # Parse assigned_entries (list from container "ASSIGNED-ENTRIES")
        obj.assigned_entries = []
        container = SerializationHelper.find_child_element(element, "ASSIGNED-ENTRIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assigned_entries.append(child_value)

        # Parse ident
        child = SerializationHelper.find_child_element(element, "IDENT")
        if child is not None:
            ident_value = child.text
            obj.ident = ident_value

        # Parse service_needs
        child = SerializationHelper.find_child_element(element, "SERVICE-NEEDS")
        if child is not None:
            service_needs_value = SerializationHelper.deserialize_by_tag(child, "ServiceNeeds")
            obj.service_needs = service_needs_value

        return obj



class BswServiceDependencyBuilder:
    """Builder for BswServiceDependency."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswServiceDependency = BswServiceDependency()

    def build(self) -> BswServiceDependency:
        """Build and return BswServiceDependency object.

        Returns:
            BswServiceDependency instance
        """
        # TODO: Add validation
        return self._obj

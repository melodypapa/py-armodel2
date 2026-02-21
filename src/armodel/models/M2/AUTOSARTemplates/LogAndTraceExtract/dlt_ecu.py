"""DltEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2018)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 8)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_application import (
    DltApplication,
)


class DltEcu(ARElement):
    """AUTOSAR DltEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applications: list[DltApplication]
    ecu_id: Optional[String]
    def __init__(self) -> None:
        """Initialize DltEcu."""
        super().__init__()
        self.applications: list[DltApplication] = []
        self.ecu_id: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DltEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltEcu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize applications (list to container "APPLICATIONS")
        if self.applications:
            wrapper = ET.Element("APPLICATIONS")
            for item in self.applications:
                serialized = ARObject._serialize_item(item, "DltApplication")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_id
        if self.ecu_id is not None:
            serialized = ARObject._serialize_item(self.ecu_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltEcu":
        """Deserialize XML element to DltEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltEcu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltEcu, cls).deserialize(element)

        # Parse applications (list from container "APPLICATIONS")
        obj.applications = []
        container = ARObject._find_child_element(element, "APPLICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.applications.append(child_value)

        # Parse ecu_id
        child = ARObject._find_child_element(element, "ECU-ID")
        if child is not None:
            ecu_id_value = child.text
            obj.ecu_id = ecu_id_value

        return obj



class DltEcuBuilder:
    """Builder for DltEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltEcu = DltEcu()

    def build(self) -> DltEcu:
        """Build and return DltEcu object.

        Returns:
            DltEcu instance
        """
        # TODO: Add validation
        return self._obj

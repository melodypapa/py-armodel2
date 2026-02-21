"""ApplicationRecordElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 261)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1997)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 43)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_composite_element_data_prototype import (
    ApplicationCompositeElementDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class ApplicationRecordElement(ApplicationCompositeElementDataPrototype):
    """AUTOSAR ApplicationRecordElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    is_optional: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ApplicationRecordElement."""
        super().__init__()
        self.is_optional: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationRecordElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationRecordElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize is_optional
        if self.is_optional is not None:
            serialized = ARObject._serialize_item(self.is_optional, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-OPTIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationRecordElement":
        """Deserialize XML element to ApplicationRecordElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationRecordElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationRecordElement, cls).deserialize(element)

        # Parse is_optional
        child = ARObject._find_child_element(element, "IS-OPTIONAL")
        if child is not None:
            is_optional_value = child.text
            obj.is_optional = is_optional_value

        return obj



class ApplicationRecordElementBuilder:
    """Builder for ApplicationRecordElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationRecordElement = ApplicationRecordElement()

    def build(self) -> ApplicationRecordElement:
        """Build and return ApplicationRecordElement object.

        Returns:
            ApplicationRecordElement instance
        """
        # TODO: Add validation
        return self._obj

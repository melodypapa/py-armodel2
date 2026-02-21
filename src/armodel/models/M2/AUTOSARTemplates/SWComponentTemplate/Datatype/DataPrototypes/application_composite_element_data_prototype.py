"""ApplicationCompositeElementDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1996)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)
from abc import ABC, abstractmethod


class ApplicationCompositeElementDataPrototype(DataPrototype, ABC):
    """AUTOSAR ApplicationCompositeElementDataPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    type_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ApplicationCompositeElementDataPrototype."""
        super().__init__()
        self.type_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationCompositeElementDataPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationCompositeElementDataPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_ref
        if self.type_ref is not None:
            serialized = ARObject._serialize_item(self.type_ref, "ApplicationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationCompositeElementDataPrototype":
        """Deserialize XML element to ApplicationCompositeElementDataPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationCompositeElementDataPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationCompositeElementDataPrototype, cls).deserialize(element)

        # Parse type_ref
        child = ARObject._find_child_element(element, "TYPE-TREF")
        if child is not None:
            type_ref_value = ARRef.deserialize(child)
            obj.type_ref = type_ref_value

        return obj



class ApplicationCompositeElementDataPrototypeBuilder:
    """Builder for ApplicationCompositeElementDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeElementDataPrototype = ApplicationCompositeElementDataPrototype()

    def build(self) -> ApplicationCompositeElementDataPrototype:
        """Build and return ApplicationCompositeElementDataPrototype object.

        Returns:
            ApplicationCompositeElementDataPrototype instance
        """
        # TODO: Add validation
        return self._obj

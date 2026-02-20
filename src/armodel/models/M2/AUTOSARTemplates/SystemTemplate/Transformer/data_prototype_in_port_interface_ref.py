"""DataPrototypeInPortInterfaceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 787)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
    DataPrototypeReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInPortInterfaceRef(DataPrototypeReference):
    """AUTOSAR DataPrototypeInPortInterfaceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_prototype_in_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceRef."""
        super().__init__()
        self.data_prototype_in_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeInPortInterfaceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeInPortInterfaceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_prototype_in_ref
        if self.data_prototype_in_ref is not None:
            serialized = ARObject._serialize_item(self.data_prototype_in_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-PROTOTYPE-IN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInPortInterfaceRef":
        """Deserialize XML element to DataPrototypeInPortInterfaceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeInPortInterfaceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeInPortInterfaceRef, cls).deserialize(element)

        # Parse data_prototype_in_ref
        child = ARObject._find_child_element(element, "DATA-PROTOTYPE-IN-REF")
        if child is not None:
            data_prototype_in_ref_value = ARRef.deserialize(child)
            obj.data_prototype_in_ref = data_prototype_in_ref_value

        return obj



class DataPrototypeInPortInterfaceRefBuilder:
    """Builder for DataPrototypeInPortInterfaceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInPortInterfaceRef = DataPrototypeInPortInterfaceRef()

    def build(self) -> DataPrototypeInPortInterfaceRef:
        """Build and return DataPrototypeInPortInterfaceRef object.

        Returns:
            DataPrototypeInPortInterfaceRef instance
        """
        # TODO: Add validation
        return self._obj

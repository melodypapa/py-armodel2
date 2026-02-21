"""NvDataInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 664)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2041)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class NvDataInterface(DataInterface):
    """AUTOSAR NvDataInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nv_data_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize NvDataInterface."""
        super().__init__()
        self.nv_data_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize NvDataInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvDataInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nv_data_refs (list to container "NV-DATA-REFS")
        if self.nv_data_refs:
            wrapper = ET.Element("NV-DATA-REFS")
            for item in self.nv_data_refs:
                serialized = ARObject._serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("NV-DATA-REF")
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
    def deserialize(cls, element: ET.Element) -> "NvDataInterface":
        """Deserialize XML element to NvDataInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvDataInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvDataInterface, cls).deserialize(element)

        # Parse nv_data_refs (list from container "NV-DATA-REFS")
        obj.nv_data_refs = []
        container = ARObject._find_child_element(element, "NV-DATA-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nv_data_refs.append(child_value)

        return obj



class NvDataInterfaceBuilder:
    """Builder for NvDataInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvDataInterface = NvDataInterface()

    def build(self) -> NvDataInterface:
        """Build and return NvDataInterface object.

        Returns:
            NvDataInterface instance
        """
        # TODO: Add validation
        return self._obj

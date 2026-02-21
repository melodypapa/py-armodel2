"""NvProvideComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class NvProvideComSpec(PPortComSpec):
    """AUTOSAR NvProvideComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ram_block_init: Optional[ValueSpecification]
    rom_block_init: Optional[ValueSpecification]
    variable_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize NvProvideComSpec."""
        super().__init__()
        self.ram_block_init: Optional[ValueSpecification] = None
        self.rom_block_init: Optional[ValueSpecification] = None
        self.variable_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize NvProvideComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvProvideComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ram_block_init
        if self.ram_block_init is not None:
            serialized = ARObject._serialize_item(self.ram_block_init, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RAM-BLOCK-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rom_block_init
        if self.rom_block_init is not None:
            serialized = ARObject._serialize_item(self.rom_block_init, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROM-BLOCK-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_ref
        if self.variable_ref is not None:
            serialized = ARObject._serialize_item(self.variable_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvProvideComSpec":
        """Deserialize XML element to NvProvideComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvProvideComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvProvideComSpec, cls).deserialize(element)

        # Parse ram_block_init
        child = ARObject._find_child_element(element, "RAM-BLOCK-INIT")
        if child is not None:
            ram_block_init_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.ram_block_init = ram_block_init_value

        # Parse rom_block_init
        child = ARObject._find_child_element(element, "ROM-BLOCK-INIT")
        if child is not None:
            rom_block_init_value = ARObject._deserialize_by_tag(child, "ValueSpecification")
            obj.rom_block_init = rom_block_init_value

        # Parse variable_ref
        child = ARObject._find_child_element(element, "VARIABLE-REF")
        if child is not None:
            variable_ref_value = ARRef.deserialize(child)
            obj.variable_ref = variable_ref_value

        return obj



class NvProvideComSpecBuilder:
    """Builder for NvProvideComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvProvideComSpec = NvProvideComSpec()

    def build(self) -> NvProvideComSpec:
        """Build and return NvProvideComSpec object.

        Returns:
            NvProvideComSpec instance
        """
        # TODO: Add validation
        return self._obj

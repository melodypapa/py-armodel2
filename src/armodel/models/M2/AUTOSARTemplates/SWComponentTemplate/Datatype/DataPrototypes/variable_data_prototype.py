"""VariableDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 107)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2077)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 256)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 29)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 223)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class VariableDataPrototype(AutosarDataPrototype):
    """AUTOSAR VariableDataPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    init_value: Optional[ValueSpecification]
    def __init__(self) -> None:
        """Initialize VariableDataPrototype."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None

    def serialize(self) -> ET.Element:
        """Serialize VariableDataPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VariableDataPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize init_value
        if self.init_value is not None:
            serialized = SerializationHelper.serialize_item(self.init_value, "ValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INIT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableDataPrototype":
        """Deserialize XML element to VariableDataPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableDataPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VariableDataPrototype, cls).deserialize(element)

        # Parse init_value
        child = SerializationHelper.find_child_element(element, "INIT-VALUE")
        if child is not None:
            init_value_value = SerializationHelper.deserialize_by_tag(child, "ValueSpecification")
            obj.init_value = init_value_value

        return obj



class VariableDataPrototypeBuilder:
    """Builder for VariableDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableDataPrototype = VariableDataPrototype()

    def build(self) -> VariableDataPrototype:
        """Build and return VariableDataPrototype object.

        Returns:
            VariableDataPrototype instance
        """
        # TODO: Add validation
        return self._obj

"""McSwEmulationMethodSupport AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_parameter_element_group import (
    McParameterElementGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class McSwEmulationMethodSupport(ARObject):
    """AUTOSAR McSwEmulationMethodSupport."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base_reference", None, False, False, VariableDataPrototype),  # baseReference
        ("category", None, True, False, None),  # category
        ("element_groups", None, False, True, McParameterElementGroup),  # elementGroups
        ("reference_table", None, False, False, VariableDataPrototype),  # referenceTable
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize McSwEmulationMethodSupport."""
        super().__init__()
        self.base_reference: Optional[VariableDataPrototype] = None
        self.category: Optional[Identifier] = None
        self.element_groups: list[McParameterElementGroup] = []
        self.reference_table: Optional[VariableDataPrototype] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert McSwEmulationMethodSupport to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McSwEmulationMethodSupport":
        """Create McSwEmulationMethodSupport from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            McSwEmulationMethodSupport instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to McSwEmulationMethodSupport since parent returns ARObject
        return cast("McSwEmulationMethodSupport", obj)


class McSwEmulationMethodSupportBuilder:
    """Builder for McSwEmulationMethodSupport."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McSwEmulationMethodSupport = McSwEmulationMethodSupport()

    def build(self) -> McSwEmulationMethodSupport:
        """Build and return McSwEmulationMethodSupport object.

        Returns:
            McSwEmulationMethodSupport instance
        """
        # TODO: Add validation
        return self._obj

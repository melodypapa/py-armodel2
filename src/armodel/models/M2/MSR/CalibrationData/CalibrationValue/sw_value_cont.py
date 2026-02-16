"""SwValueCont AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_unit_names import (
    SingleLanguageUnitNames,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_values import (
    SwValues,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class SwValueCont(ARObject):
    """AUTOSAR SwValueCont."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_arraysize", None, False, False, ValueList),  # swArraysize
        ("sw_values_phys", None, False, False, SwValues),  # swValuesPhys
        ("unit", None, False, False, Unit),  # unit
        ("unit_display", None, False, False, SingleLanguageUnitNames),  # unitDisplay
    ]

    def __init__(self) -> None:
        """Initialize SwValueCont."""
        super().__init__()
        self.sw_arraysize: Optional[ValueList] = None
        self.sw_values_phys: Optional[SwValues] = None
        self.unit: Optional[Unit] = None
        self.unit_display: Optional[SingleLanguageUnitNames] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwValueCont to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwValueCont":
        """Create SwValueCont from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwValueCont instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwValueCont since parent returns ARObject
        return cast("SwValueCont", obj)


class SwValueContBuilder:
    """Builder for SwValueCont."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwValueCont = SwValueCont()

    def build(self) -> SwValueCont:
        """Build and return SwValueCont object.

        Returns:
            SwValueCont instance
        """
        # TODO: Add validation
        return self._obj

"""McFunction AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_function import (
    McFunction,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.mc_function_data_ref_set import (
    McFunctionDataRefSet,
)


class McFunction(ARElement):
    """AUTOSAR McFunction."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("def_calprm_set", None, False, False, McFunctionDataRefSet),  # defCalprmSet
        ("in_measurement", None, False, False, McFunctionDataRefSet),  # inMeasurement
        ("loc", None, False, False, McFunctionDataRefSet),  # loc
        ("out", None, False, False, McFunctionDataRefSet),  # out
        ("ref_calprm_set", None, False, False, McFunctionDataRefSet),  # refCalprmSet
        ("sub_functions", None, False, True, McFunction),  # subFunctions
    ]

    def __init__(self) -> None:
        """Initialize McFunction."""
        super().__init__()
        self.def_calprm_set: Optional[McFunctionDataRefSet] = None
        self.in_measurement: Optional[McFunctionDataRefSet] = None
        self.loc: Optional[McFunctionDataRefSet] = None
        self.out: Optional[McFunctionDataRefSet] = None
        self.ref_calprm_set: Optional[McFunctionDataRefSet] = None
        self.sub_functions: list[McFunction] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert McFunction to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McFunction":
        """Create McFunction from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            McFunction instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to McFunction since parent returns ARObject
        return cast("McFunction", obj)


class McFunctionBuilder:
    """Builder for McFunction."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McFunction = McFunction()

    def build(self) -> McFunction:
        """Build and return McFunction object.

        Returns:
            McFunction instance
        """
        # TODO: Add validation
        return self._obj

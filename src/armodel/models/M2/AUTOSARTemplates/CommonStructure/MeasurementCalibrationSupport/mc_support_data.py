"""McSupportData AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_sw_emulation_method_support import (
    McSwEmulationMethodSupport,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_support_data import (
    RptSupportData,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)


class McSupportData(ARObject):
    """AUTOSAR McSupportData."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("emulations", None, False, True, McSwEmulationMethodSupport),  # emulations
        ("mc_parameters", None, False, True, McDataInstance),  # mcParameters
        ("mc_variables", None, False, True, McDataInstance),  # mcVariables
        ("measurables", None, False, True, SwSystemconstantValueSet),  # measurables
        ("rpt_support_data", None, False, False, RptSupportData),  # rptSupportData
    ]

    def __init__(self) -> None:
        """Initialize McSupportData."""
        super().__init__()
        self.emulations: list[McSwEmulationMethodSupport] = []
        self.mc_parameters: list[McDataInstance] = []
        self.mc_variables: list[McDataInstance] = []
        self.measurables: list[SwSystemconstantValueSet] = []
        self.rpt_support_data: Optional[RptSupportData] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert McSupportData to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McSupportData":
        """Create McSupportData from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            McSupportData instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to McSupportData since parent returns ARObject
        return cast("McSupportData", obj)


class McSupportDataBuilder:
    """Builder for McSupportData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: McSupportData = McSupportData()

    def build(self) -> McSupportData:
        """Build and return McSupportData object.

        Returns:
            McSupportData instance
        """
        # TODO: Add validation
        return self._obj

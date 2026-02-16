"""SwCalprmRefProxy AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)


class SwCalprmRefProxy(ARObject):
    """AUTOSAR SwCalprmRefProxy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ar_parameter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarParameterRef,
        ),  # arParameter
        "mc_data_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=McDataInstance,
        ),  # mcDataInstance
    }

    def __init__(self) -> None:
        """Initialize SwCalprmRefProxy."""
        super().__init__()
        self.ar_parameter: Optional[AutosarParameterRef] = None
        self.mc_data_instance: Optional[McDataInstance] = None


class SwCalprmRefProxyBuilder:
    """Builder for SwCalprmRefProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwCalprmRefProxy = SwCalprmRefProxy()

    def build(self) -> SwCalprmRefProxy:
        """Build and return SwCalprmRefProxy object.

        Returns:
            SwCalprmRefProxy instance
        """
        # TODO: Add validation
        return self._obj

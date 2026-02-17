"""SwVariableRefProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DatadictionaryProxies.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
        McDataInstance,
    )



class SwVariableRefProxy(ARObject):
    """AUTOSAR SwVariableRefProxy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "autosar_variable_ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarVariableRef,
        ),  # autosarVariableRef
        "mc_data_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class="McDataInstance",
        ),  # mcDataInstance
    }

    def __init__(self) -> None:
        """Initialize SwVariableRefProxy."""
        super().__init__()
        self.autosar_variable_ref: Optional[AutosarVariableRef] = None
        self.mc_data_instance: Optional[McDataInstance] = None


class SwVariableRefProxyBuilder:
    """Builder for SwVariableRefProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwVariableRefProxy = SwVariableRefProxy()

    def build(self) -> SwVariableRefProxy:
        """Build and return SwVariableRefProxy object.

        Returns:
            SwVariableRefProxy instance
        """
        # TODO: Add validation
        return self._obj

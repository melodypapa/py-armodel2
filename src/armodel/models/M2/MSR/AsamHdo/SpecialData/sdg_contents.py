"""SdgContents AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sd import (
    Sd,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdf import (
    Sdf,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
        Sdg,
    )



class SdgContents(ARObject):
    """AUTOSAR SdgContents."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sd: Optional[Sd]
    sdf: Optional[Sdf]
    sdg: Optional[Sdg]
    sdx_ref: Optional[ARRef]
    sdxf_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SdgContents."""
        super().__init__()
        self.sd: Optional[Sd] = None
        self.sdf: Optional[Sdf] = None
        self.sdg: Optional[Sdg] = None
        self.sdx_ref: Optional[ARRef] = None
        self.sdxf_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgContents":
        """Deserialize XML element to SdgContents object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgContents object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sd
        child = ARObject._find_child_element(element, "SD")
        if child is not None:
            sd_value = ARObject._deserialize_by_tag(child, "Sd")
            obj.sd = sd_value

        # Parse sdf
        child = ARObject._find_child_element(element, "SDF")
        if child is not None:
            sdf_value = ARObject._deserialize_by_tag(child, "Sdf")
            obj.sdf = sdf_value

        # Parse sdg
        child = ARObject._find_child_element(element, "SDG")
        if child is not None:
            sdg_value = ARObject._deserialize_by_tag(child, "Sdg")
            obj.sdg = sdg_value

        # Parse sdx_ref
        child = ARObject._find_child_element(element, "SDX")
        if child is not None:
            sdx_ref_value = ARObject._deserialize_by_tag(child, "Referrable")
            obj.sdx_ref = sdx_ref_value

        # Parse sdxf_ref
        child = ARObject._find_child_element(element, "SDXF")
        if child is not None:
            sdxf_ref_value = ARObject._deserialize_by_tag(child, "Referrable")
            obj.sdxf_ref = sdxf_ref_value

        return obj



class SdgContentsBuilder:
    """Builder for SdgContents."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgContents = SdgContents()

    def build(self) -> SdgContents:
        """Build and return SdgContents object.

        Returns:
            SdgContents instance
        """
        # TODO: Add validation
        return self._obj

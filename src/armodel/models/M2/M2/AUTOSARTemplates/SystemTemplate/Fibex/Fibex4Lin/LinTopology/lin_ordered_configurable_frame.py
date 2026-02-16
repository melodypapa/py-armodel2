"""LinOrderedConfigurableFrame AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)


class LinOrderedConfigurableFrame(ARObject):
    """AUTOSAR LinOrderedConfigurableFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "frame": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LinFrame,
        ),  # frame
        "index": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # index
    }

    def __init__(self) -> None:
        """Initialize LinOrderedConfigurableFrame."""
        super().__init__()
        self.frame: Optional[LinFrame] = None
        self.index: Optional[Integer] = None


class LinOrderedConfigurableFrameBuilder:
    """Builder for LinOrderedConfigurableFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinOrderedConfigurableFrame = LinOrderedConfigurableFrame()

    def build(self) -> LinOrderedConfigurableFrame:
        """Build and return LinOrderedConfigurableFrame object.

        Returns:
            LinOrderedConfigurableFrame instance
        """
        # TODO: Add validation
        return self._obj
